class product:
    id = ''
    brandName = ''
    price = ''
    Discription = ''
    returnPolicy = ''
    instalment = ''
    Discount = ''
    seller_Name = ''

    def __init__(self, id, br_name, pr, discription, discount, r_policy, instalment, s_name):
        self.id = id
        self.brandName = br_name
        self.price = pr
        self.Discription = discription
        self.Discount = discount
        self.returnPolicy = r_policy
        self.instalment = instalment
        self.seller_Name = s_name

    def init(self, id):
        self.id = id,

    def init(self, br_name):
        self.brandName = br_name

    def init(self, pr):
        self.price = pr

    def init(self, disc):
        self.Discription = disc

    def init(self, discount):
        self.Discount = discount

    def init(self, r_policy):
        self.returnPolicy = r_policy

    def init(self, s_name):
        self.seller_Name = s_name

    def init(self, instalment):
        self.instalment = instalment
