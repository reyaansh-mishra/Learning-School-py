'''Write a func named slice_it(numbers: list, index: int)
        Divide before and after index'''

def slice_it(numbers: list[int], index: int):
        prev_queue: list[int]      = []
        after_queue: list[int]     = []

        use_prev_queue: bool    = True

        for i in numbers:
                if (i == index):
                        use_prev_queue = False        

                if (use_prev_queue):
                        prev_queue.append(i)
                else:
                        after_queue.append(i)

        return prev_queue, after_queue