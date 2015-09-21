__author__ = 'luisdiegopizarro'
class Movement:
    '''
    movement cost
    tower state
    movement action
    movement direction 1up 2 down 3 left 4 right
    column-row to move
    '''

    def __init__(self,pCost,pMov,pDescription,pDirection,pPosition):
        self.cost=pCost
        self.tower=pMov
        self.description=pDescription
        self.direction=pDirection
        self.position=pPosition