import random

card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
cards = [random.choice(card_list) for i in range(2)]

print('Attempt to beat the dealer by getting a count as close to 21 as possible, without going over 21.')

hand = []
sum_hand = []
d_hand = []
sum_d_hand = []

def main():
    print(starting_hand())
    print(starting_d_hand())
    resume = True
    player_resume = True  
    while resume:
        if sum(sum_hand) == 21 and len(hand) == 2 or sum(sum_d_hand) == 21 and len(d_hand) == 2:
            print(f'You: {hand} {sum(sum_hand)}')
            print(f'Dealer: {d_hand} {sum(sum_d_hand)}')
            break
        if sum(sum_hand) == 21 or sum(sum_d_hand) == 21:
            break
        if sum(sum_d_hand) < 17:
            convert(d_hit(), d_hand)
        if player_resume:
            while True:
                try:
                    decision = input("'y' for hit or 'n' for stand ")
                    if decision not in ('y', 'n'):
                        raise ValueError
                except ValueError:
                    print("type 'y' or 'n'")
                else:
                    break
            if decision == 'y':
                convert(hit(), hand)
            else:
                player_resume = False
            if sum(sum_hand) >= 21:
                player_resume = False
                
        print(f'You: {hand} {sum(sum_hand)}')
        print(f'Dealer: {d_hand} {sum(sum_d_hand)}')
        if player_resume is False and sum(sum_d_hand) >= 17:
            resume = False
    print(check_winner(sum(sum_hand), sum(sum_d_hand)))    

def starting_hand():
    for i in range(2):
        convert(hit(), hand)
    return f'You: {hand} {sum(sum_hand)}'


def starting_d_hand():
    for i in range(2):
        convert(d_hit(), d_hand)        
    return f'Dealer: {[d_hand[0]]}'


def hit():
    card = random.choice(card_list)
    hand.append(card)
    card_list.remove(card)
    return card

def d_hit():
    card = random.choice(card_list)
    d_hand.append(card)
    card_list.remove(card)
    return card


def convert(card, hands):
    if hands == hand:
        if type(card) == int:
            sum_hand.append(card)
            return card
        elif card in ('J', 'Q', 'K'):
            sum_hand.append(10)
            return 10
        elif card == 'A':
            if sum(sum_hand) + 11 > 21:
                sum_hand.append(1)
                return 1
            else:
                sum_hand.append(11)
                return 11
    
    if hands == d_hand:
        if type(card) == int:
            sum_d_hand.append(card)
            return card
        elif card in ('J', 'Q', 'K'):
            sum_d_hand.append(10)
            return 10
        elif card == 'A':
            if sum(sum_d_hand) + 11 > 21:
                sum_d_hand.append(1)
                return 1
            else:
                sum_d_hand.append(11)
                return 11

def check_winner(player, dealer):
    if player > dealer and player <= 21 or player <= 21 and dealer > 21:
        return 'You Win'
    elif player < dealer and dealer <= 21 or player > 21 and dealer <= 21:
        return 'Dealer Wins'
    elif player > 21 and dealer > 21 or player == dealer:
        return 'No Winner'

if __name__ == '__main__':
    main()

'''if sum(sum_hand) == 21 and len(hand) == 2 or sum(sum_d_hand) == 21 and len(d_hand) == 2:
            
        while True:
            try:
                decision = input("'y' for hit or 'n' for stand ")
                if decision not in ('y', 'n'):
                    raise ValueError
            except ValueError:
                print("type 'y' or 'n'")
            else:
                break
        if decision == 'y':
            convert(hit(), hand)
        else:
            player_resume = False
        if sum(sum_hand) >= 21:
            player_resume = False        
    
    while sum(sum_d_hand) <= 21:
        if sum(sum_d_hand) >= 17:
            break
        convert(d_hit(), d_hand)
        print(f'You: {hand} {sum(sum_hand)}')
        print(f'Dealer: {d_hand} {sum(sum_d_hand)}')

    if sum(sum_d_hand) >= 17 and player_resume is False:
        resume = False
    print(check_winner(sum(sum_hand), sum(sum_d_hand)))'''