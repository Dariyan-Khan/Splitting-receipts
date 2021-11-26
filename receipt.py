from argparse import ArgumentParser
def build_parser():
    parser = ArgumentParser()

    parser.add_argument('--A',
                        dest='A_spent', help='amount dariyan spent',
                        metavar='A', required=True)

    parser.add_argument('--B',
                        dest='B_spent', help='amount leo spent',
                        metavar='B', required=True)

    parser.add_argument('--C',
                        dest='C_spent', help='amount will spent',
                        metavar='C', required=True)

    return parser


def main():

    parser = build_parser()
    options = parser.parse_args()

    spent_dict={}
    d_spent=float(options.A_spent)
    l_spent=float(options.B_spent)
    w_spent=float(options.C_spent)



    spent_dict[d_spent]='A'
    spent_dict[l_spent]='B'
    spent_dict[w_spent]='C'


    payment_list=[d_spent,l_spent,w_spent]

    sorted_payment_list=sorted(payment_list)

    sorted_people=[spent_dict[i] for i in sorted_payment_list]

    avg_payment=sum(sorted_payment_list)/3.0

    print('This is the average: {}'.format(avg_payment) + '\n')

    if sorted_payment_list[1] <= avg_payment:

        print( '{} pays {} £{}'.format(sorted_people[0],sorted_people[2],avg_payment-sorted_payment_list[0]) + '\n')

        print('{} pays {} £{}'.format(sorted_people[1], sorted_people[2], avg_payment - sorted_payment_list[1]) + '\n')

    else:

        print('{} pays {} £{}'.format(sorted_people[0], sorted_people[1],
                                      sorted_payment_list[1]-avg_payment) + '\n')

        print('{} pays {} £{}'.format(sorted_people[0], sorted_people[2],
                                      sorted_payment_list[2] - avg_payment) + '\n')

if __name__ == '__main__':
    main()










