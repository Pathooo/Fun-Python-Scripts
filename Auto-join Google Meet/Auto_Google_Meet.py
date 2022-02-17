#To automate loggin into google meetings for online classes because i forget to join on time :))

# import modules
import webbrowser		# automate browser opening
import pyautogui       # automate clicks
import time				# delay between clicks
import schedule			# schedule timings like cron


class Gmeet:

	def __init__(self,filename):
		self.codes={}
		self.filename=filename

	def join_meet(slef,code):

		"""Opens meet window using given code and joins it"""

		url=f"https://meet.google.com/{code}"
		webbrowser.open_new(url)
		time.sleep(5)

		pyautogui.hotkey('ctrl','d')
		pyautogui.hotkey('ctrl','e')
		time.sleep(1)

		pyautogui.moveTo(1355,578)
		pyautogui.click()

	def start_script(self):

		"""Opens the file and schedules the task of joining meet at given time with given code"""

		with open(self.filename,'r') as f:
			for line in f:
				self.codes[line.split('\t')[0]]=line.split('\t')[1]

		for code,time in self.codes.items():
			schedule.every().monday.at(time).do(self.join_meet(code))
			# We can add more days with times as required
			#self.join_meet(code)

gmeet_joiner=Gmeet('codes.txt')
gmeet_joiner.start_script()



