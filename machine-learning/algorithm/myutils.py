# 정확도, 정밀도, 재현율 출력 함수 
def print_score(y_true, y_pred, average='binary'):    
    acc = accuracy_score(y_true, y_pred) 
    pre = precision_score(y_true, y_pred, average = average)
    rec = recall_score(y_true, y_pred, average = average)
    
    print('accuraccy:', acc)
    print('precision:', pre)
    print('recall:', rec)