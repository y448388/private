def fun__assignment_e2_b_main():
    # try:
        def fun__assignment_e2_b(var__int__n1, var__int__n2):
            # try:
                # if not isinstance(var__int__n1, int) or not isinstance(var__int__n2, int):
                    # raise ValueError("Error message.")
                var__int__e2_r1 = var__int__n1 + var__int__n2
                var__int__e2_r2 = var__int__n1 - var__int__n2
                var__int__e2_r3 = var__int__n1 * var__int__n2
                if var__int__n2 != 0:
                    var__float__e2_r4 = var__int__n1 / var__int__n2
                    # var__int__e2_r4_r = int(round(var__int__n1 / var__int__n2, 0))
                else:
                    var__float__e2_r4 = "error"
                print ("\na: {}\nb: {}\na + b: {}\na - b: {}\na * b: {}\na / b: {}".format(var__int__n1,var__int__n2,var__int__e2_r1,var__int__e2_r2,var__int__e2_r3,var__float__e2_r4))
            # except:
                # print("Error message.")
        
        # fun__assignment_e2_b(input("Input a arbitrary precision integer: "), input("Input another arbitrary precision integer: "))
        # fun__assignment_e2_b(255, -128)
        fun__assignment_e2_b(65535, -32768)
    # except:
        # print("Error message.")
