from s3_1 import run

train = 'TrainSet 2'
test = 'TestSet 2'

if __name__ == '__main__':
    run(train, test, 's3_1_b_1to10inc1.log', 1, 11, 1)
    run(train, test, 's3_1_b_15to100inc5.log', 15, 101, 5)
