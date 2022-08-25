import os 
import argparse 


class Addition:
    
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def add_two_numbers(self):
        result = 0
        add = self.num1 + self.num2
        result += add
        return result
    
    def minus_two_number(self):
        return self.num1 - self.num2
    
    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                print('folder created')
            else:
                print('Folder already exist')
                
        except OSError as e:
            print('Folder cannot be created', e)

    def create_dict(self, nums):
        num_dict = {}
        
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        return num_dict
        
        
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num1', dest='first_num', type=int, required=False)
    parser.add_argument('--num2', dest='second_num', type=int, required=False)
    parser.add_argument('--path', dest='file_path', type=str, required=False)
    parser.add_argument('--nums', dest='nums', nargs='+', required=True)
    
    args = parser.parse_args()
      
    first_number = Addition(args.first_num, args.second_num)
    
    # print(getattr(first_number, 'num3', 9))    
    # print(first_number.add_two_numbers())
    first_number.create_directory(args.file_path)
    print(first_number.create_dict(args.nums))


if __name__ == '__main__':
    main()
    