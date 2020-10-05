from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Normally the routes would not be in init.py for the exercise
@app.route('/calculate_fibonacci', methods=['GET'])
def calc_fibonacci():
    num = request.args.get("num", None)
    if not num:
        raise BadRequest("Please provide the number param.")
    try:
        num = int(num)
    except Exception as e:
        raise BadRequest("The number is not a valid integer for {0} with error {1}".format(num,str(e)))

    fib_num_list = []
    for i in range(num+1):
        if i == 0 or i == 1:
            fib_num_list.append(i)
        else:
            fib_num = fib_num_list[i-1]+fib_num_list[i-2]
            fib_num_list.append(fib_num)
    return "The fibonacci sequence is {} for the number: {}".format(str(fib_num_list), num)

if __name__ == '__main__':
    app.run()
