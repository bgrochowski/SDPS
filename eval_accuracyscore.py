import pickle

accuracies = [0 for i in range(15)]
total_acc = 0


#open results pickle file
with open('results_evaluation.pkl', 'rb') as f:
    results = pickle.load(f)
    # print(len(results))
    for i in range(15):
        for j in range(len(results[i])):
            outcome = results[i][j][:2]
            if outcome == 'Ye' or outcome == 'ye':
                accuracies[i]+=1
                total_acc+=1
            elif outcome == 'No' or outcome == 'no':
                pass
            else:
                print(results[i][j])
                uncertain = input("Is this a correct prediction? (y/n)")
                if uncertain == 'y':
                    accuracies[i]+=1
                    total_acc+=1
                elif uncertain == 'n':
                    pass
        accuracies[i] = accuracies[i]/len(results[i])
        print(accuracies[i])

total_acc = total_acc/130
print("total accuracy: ", total_acc)