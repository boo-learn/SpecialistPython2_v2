class Money:
    def __init__(self, rubli, kopeyki):
        self.rubli = rubli
        self.kopeyki = kopeyki

    def __str__(self):
        return f'{self.rubli} rub. {self.kopeyki} kop.'

    def perevod_v_rubli(self):
        while self.kopeyki >100:
            if self.kopeyki > 100:
                self.kopeyki -= 100
                self.rubli += 1
