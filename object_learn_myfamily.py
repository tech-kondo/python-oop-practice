# coding: UTF-8
"""このプログラムはオブジェクト指向を意識して書いたPythonプログラムです"""

class Family:
	"""docstring for Family"""
	def __init__(self, name):
		self.name = name
		self.destination = None

	def have_meal(self, talk):
		print(f"{self.name}は「{talk}」と言った。")

	def go_out(self, spent_time, destination):
		self.destination = destination
		print(f"{self.name}は今日{spent_time}分かけて{self.destination}へ行く。")

	def plan_day(self):
		if self.destination:
			print(f"{self.name}は今日は{self.destination}で過ごす予定。")
		else:
			print(f"{self.name}は今日は特に予定なし。")

	def sleep(self):
		print(f"{self.name}は「おやすみなさい。」と言って寝室に向かった。")


kondo_mother = Family("ひろみ")
kondo_father = Family("あきお")
kondo_brother = Family("じんた")
kondo_sister = Family("ゆうな")
kondo_cute_dog = Family("ぶるた")
kondo_me = Family("あいな")

print("食事の時間だ。")

kondo_mother.have_meal("温かいうちに食べて。")
kondo_father.have_meal("なんや？なんかご馳走やないか")
kondo_brother.have_meal("あと10分待って！もう終わるから！")
kondo_sister.have_meal("いただきまぁす～")
kondo_cute_dog.have_meal("ぶひぶひ")
kondo_me.have_meal("美味しそう！！")

print("朝が来た。")

kondo_father.go_out(30, "会社")
kondo_brother.go_out(15, "高校")
kondo_sister.go_out(35, "友達の家")

kondo_father.plan_day()
kondo_cute_dog.plan_day()

kondo_me.sleep()