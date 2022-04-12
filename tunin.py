""" 2-1. GET BASE DATA """
import joblib
import os
base = os.path.dirname(os.path.abspath(__file__))
# stock = joblib.load(os.path.join(base,'target','stock'))
stock = 'TSLA' # 코드 전체 작성 후 자동화 완료시 삭제
df = joblib.load(os.path.join(base,'data',stock)) #1

# 1. stock 이름을 가지는 저장된 DATA -> df 변수


""" 2-2. TRAIN-TEST SPLIT """
train = df[0:int(len(df)*0.75)] #1
test = df[int(len(df)*0.75):]
features = ['Search','Price','Open','High','Low','Vol','Change','avg_one','avg_thr','avg_fiv'] #2

# 1. 75%는 train, 나머지는 test로 데이터 분할
# 2. 예측에 활용할 Feature 값 저장


# Train Data Set - X_train = 예측에 활용(Feature), Y_train = 실제 결과값(Target)
X_train = train[features]
y_train_1 = train['one']
y_train_2 = train['two']
y_train_3 = train['thr']
y_train_4 = train['for']
y_train_5 = train['fiv']
y_train_6 = train['six']
y_train_7 = train['sev']
y_train_8 = train['eig']
y_train_9 = train['nin']
y_train_10 = train['ten']

# Test Data Set_1 - Test 데이터는 끝 부분에 결측치가 있어서 해당 결측치를 제거해줘야 함
X_test_1 = test[features]
X_test_1 = X_test_1[:-1]
y_test_1 = test['one']
y_test_1 = y_test_1[:-1]

# Test Data Set_2
X_test_2 = test[features]
X_test_2 = X_test_2[:-2]
y_test_2 = test['two']
y_test_2 = y_test_2[:-2]

# Test Data Set_3
X_test_3 = test[features]
X_test_3 = X_test_3[:-3]
y_test_3 = test['thr']
y_test_3 = y_test_3[:-3]

# Test Data Set_4
X_test_4 = test[features]
X_test_4 = X_test_4[:-4]
y_test_4 = test['for']
y_test_4 = y_test_4[:-4]

# Test Data Set_5
X_test_5 = test[features]
X_test_5 = X_test_5[:-5]
y_test_5 = test['fiv']
y_test_5 = y_test_5[:-5]

# Test Data Set_6
X_test_6 = test[features]
X_test_6 = X_test_6[:-6]
y_test_6 = test['six']
y_test_6 = y_test_6[:-6]

# Test Data Set_7
X_test_7 = test[features]
X_test_7 = X_test_7[:-7]
y_test_7 = test['sev']
y_test_7 = y_test_7[:-7]

# Test Data Set_8
X_test_8 = test[features]
X_test_8 = X_test_8[:-8]
y_test_8 = test['eig']
y_test_8 = y_test_8[:-8]

# Test Data Set_9
X_test_9 = test[features]
X_test_9 = X_test_9[:-9]
y_test_9 = test['nin']
y_test_9 = y_test_9[:-9]

# Test Data Set_10
X_test_10 = test[features]
X_test_10 = X_test_10[:-10]
y_test_10 = test['ten']
y_test_10 = y_test_10[:-10]


""" 2-3. PARAMETER TUNING """
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
params = { 'n_estimators' : [10,100],
           'max_depth' : [ 2, 4, 8, 16],
           'min_samples_leaf' : [1,3,5],
           'min_samples_split' : [ 2,4,8, 16]
            }

rf_clf = RandomForestClassifier(random_state = 0, n_jobs = -1)
grid_cv = GridSearchCV(rf_clf, param_grid = params, cv = 3, n_jobs = -1)

print("grid search 진행중 . . . ")

grid_cv.fit(X_train, y_train_1)
p1 = grid_cv.best_params_
print('1주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('1주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_2)
p2 = grid_cv.best_params_
print('2주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('2주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_3)
p3 = grid_cv.best_params_
print('3주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('3주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_4)
p4 = grid_cv.best_params_
print('4주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('4주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_5)
p5 = grid_cv.best_params_
print('5주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('5주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_6)
p6 = grid_cv.best_params_
print('6주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('6주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_7)
p7 = grid_cv.best_params_
print('7주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('7주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_8)
p8 = grid_cv.best_params_
print('8주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('8주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_9)
p9 = grid_cv.best_params_
print('9주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('9주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

grid_cv.fit(X_train, y_train_10)
p10 = grid_cv.best_params_
print('10주 최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('10주 최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))


""" 2-4. SEND & SAVE PARAMETERS """
joblib.dump(p1, os.path.join(base,'param','p1'))
joblib.dump(p2, os.path.join(base,'param','p2'))
joblib.dump(p3, os.path.join(base,'param','p3'))
joblib.dump(p4, os.path.join(base,'param','p4'))
joblib.dump(p5, os.path.join(base,'param','p5'))
joblib.dump(p6, os.path.join(base,'param','p6'))
joblib.dump(p7, os.path.join(base,'param','p7'))
joblib.dump(p8, os.path.join(base,'param','p8'))
joblib.dump(p9, os.path.join(base,'param','p9'))
joblib.dump(p10, os.path.join(base,'param','p10'))

# 파라미터 폴더안에 pickle화 해서 변수 저장