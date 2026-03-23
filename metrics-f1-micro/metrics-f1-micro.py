def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    pass

    from collections import defaultdict

    TP = 0
    FN = 0
    FP = defaultdict(int)

    sz = len(y_true)
    for i in range(sz):
        if (y_true[i] != y_pred[i]): 
            FP[y_pred[i]] += 1
        else:
            TP += 1
    
    FN = sz - TP
    
    FP_count = 0
    for x, y in FP.items():
        # print(x, y)
        FP_count += y
    print(TP, FN, FP_count)
    return (2 * TP / (2 * TP + FP_count + FN))

def main():
    # Main logic of your program goes here
    y_true = [2,2,1,0]
    y_pred = [1,2,1,0]
    print(f1_micro(y_true, y_pred))

if __name__ == "__main__":
    main()
