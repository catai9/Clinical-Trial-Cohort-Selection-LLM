import pandas as pd
from sklearn.metrics import f1_score

def evaluation(reference_df, prediction_df, tasks):
    """
    Returns
    -------
    scores: dict
        A dictionary of all metrics and string representation of the metrics.
    """
    scores = {}
    for task in tasks:
        task_name = task.get_task_name()
        preds = prediction_df[prediction_df[task_name].notnull()]
        merge = pd.merge(reference_df[["id", task_name]], preds, on="id", suffixes=["_ref", "_pred"])
        default_value = task.get_default_class()
        pred_col = task_name + "_pred"
        ref_col = task_name + "_ref"
        merge['tp'] = merge.apply(lambda r: 1 if r[ref_col] != default_value and r[ref_col] == r[pred_col] else 0, axis=1)
        merge['fp'] = merge.apply(lambda r: 1 if r[ref_col] == default_value and r[ref_col] != r[pred_col] else 0, axis=1)
        merge['tn'] = merge.apply(lambda r: 1 if r[ref_col] == default_value and r[ref_col] == r[pred_col] else 0, axis=1)
        merge['fn'] = merge.apply(lambda r: 1 if r[ref_col] != default_value and r[ref_col] != r[pred_col] else 0, axis=1)
        all_tp = merge['tp'].sum()
        all_fp = merge['fp'].sum()
        all_fn = merge['fn'].sum()
        all_tn = merge['tn'].sum()
        if all_tp == 0:
            precision = 0
            recall = 0
            f1_score = 0
        else:
            precision = all_tp / (all_tp + all_fp)            
            recall = all_tp / (all_tp + all_fn)
            f1_score = (2 * precision * recall) / (precision + recall)
        if len(merge):
            acc = (all_tp + all_tn) / len(merge)
        else:
            acc = 0
        acc_str = f'{all_tp + all_tn}/{len(merge)}={acc:.2f}'
        prec_str = f'{all_tp}/{(all_tp + all_fp)}={precision:.2f}'
        rec_str = f'{all_tp}/{(all_tp + all_fn)}={recall:.2f}'
        scores[task_name] = {
            "accuracy": acc,
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "acc_str": acc_str,
            "prec_str": prec_str,
            "rec_str": rec_str
        }
    return scores


def evaluation_expanded(reference_df, prediction_df, tasks, is_multiclass=False):
    """
    Returns
    -------
    scores: dict
        A dictionary of all metrics and string representation of the metrics.
    """
    scores = {}
    for task in tasks:
        task_name = task.get_task_name()
        preds = prediction_df[prediction_df[task_name].notnull()]
        refs = reference_df[reference_df[task_name].notnull()]
        merge = pd.merge(refs[["id", task_name]], preds, on="id", suffixes=["_ref", "_pred"])
        default_value = task.get_default_class()
        pred_col = task_name + "_pred"
        ref_col = task_name + "_ref"
        
        if task_name == "ALL-SMOKER-CLASSES" or is_multiclass:
            if is_multiclass:
                merge[ref_col].replace('Y', 0, inplace=True)
                merge[ref_col].replace('N', 1, inplace=True)
                merge[ref_col].replace('Q', 2, inplace=True)
                merge[ref_col].replace('U', 3, inplace=True)
                merge[pred_col].replace('Y', 0, inplace=True)
                merge[pred_col].replace('N', 1, inplace=True)
                merge[pred_col].replace('Q', 2, inplace=True)
                merge[pred_col].replace('U', 3, inplace=True)
            
            scores[task_name] = evaluation_multiclass(merge[ref_col], merge[pred_col])
        else:
            merge['tp'] = merge.apply(lambda r: 1 if r[ref_col] != default_value and r[ref_col] == r[pred_col] else 0, axis=1)
            merge['fp'] = merge.apply(lambda r: 1 if r[ref_col] == default_value and r[ref_col] != r[pred_col] else 0, axis=1)
            merge['tn'] = merge.apply(lambda r: 1 if r[ref_col] == default_value and r[ref_col] == r[pred_col] else 0, axis=1)
            merge['fn'] = merge.apply(lambda r: 1 if r[ref_col] != default_value and r[ref_col] != r[pred_col] else 0, axis=1)
            all_tp = merge['tp'].sum()
            all_fp = merge['fp'].sum()
            all_fn = merge['fn'].sum()
            all_tn = merge['tn'].sum()
            if all_tp == 0:
                precision = 0
                recall = 0
                f1_score = 0
            else:
                precision = all_tp / (all_tp + all_fp)            
                recall = all_tp / (all_tp + all_fn)
                f1_score = (2 * precision * recall) / (precision + recall)
            if len(merge):
                acc = (all_tp + all_tn) / len(merge)
            else:
                acc = 0
            acc_str = f'{all_tp + all_tn}/{len(merge)}={acc}'
            prec_str = f'{all_tp}/{(all_tp + all_fp)}={precision}'
            rec_str = f'{all_tp}/{(all_tp + all_fn)}={recall}'
            scores[task_name] = {
                "accuracy": acc,
                "precision": precision,
                "recall": recall,
                "f1_score": f1_score,
                "acc_str": acc_str,
                "prec_str": prec_str,
                "rec_str": rec_str,
                "tp": all_tp,
                "fp": all_fp,
                "tn": all_tn,
                "fn": all_fn
            }
    return scores


def evaluation_multiclass(reference_col, prediction_col):    
    macro_f1_score = f1_score(reference_col, prediction_col, average='macro')
    micro_f1_score = f1_score(reference_col, prediction_col, average='micro')
    none_f1_score = f1_score(reference_col, prediction_col, average=None)
    
    return {
            "macro_f1_score": macro_f1_score,
            "micro_f1_score": micro_f1_score,
            "none_f1_score": none_f1_score
            }