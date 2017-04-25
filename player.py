class Player:
    name = None
    is_Vanya_met = False

    def meet_Vanya(self):
        self.is_Vanya_met = True

    def check_Vanya(self):
        return self.is_Vanya_met
