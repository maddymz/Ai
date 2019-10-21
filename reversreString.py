class ReverseWors:
    def __init__(self):
        pass


    def reverse(self, string):
        arr = []
        ns = string.split(' ')

        for i in range(len(ns)):
            element = ns[i][::-1]
            arr.append(element)

        
        return " ".join(arr)

    def rev(self, array):
        arr = []
        for i in range(len(array)):
            el = array[i]
        
        for i in range(len(array)):
            arr.append(el)

        return arr

if __name__ == "__main__":

    obj = ReverseWors()

    string = "Let's take LeetCode contest"

    print(obj.reverse(string))
    print(obj.rev(["h","e","l","l","o"]))
