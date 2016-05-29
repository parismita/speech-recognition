import speech_recognition as sr
import pyttsx
from textblob import TextBlob

r = sr.Recognizer()
m = sr.Microphone()
speaker = pyttsx.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate',rate-50)

try:
	print("A moment of silence, please...")
	with m as source: r.adjust_for_ambient_noise(source)
	print("Set minimum energy threshold to {}".format(r.energy_threshold))
	while True:
		print("Say something!")
		with m as source: audio = r.listen(source)
		#print("Got it! Now to recognize it...")
		try:
			# recognize speech using Google Speech Recognition
			#value = r.recognize_google(audio)

			# we need some special handling here to correctly print unicode characters to standard output
			if str is bytes: # this version of Python uses bytes for strings (Python 2)
				# formatted_str = format(value).encode("utf-8")
				formatted_str = "Hey ! Whats up!lets talk! "
				in_string = tr_blob.translate(to='es')
				speaker.say(in_string)
				with m as source: audio = r.listen(source)
				print("Got it! Now to recognize it...")
				value = r.recognize_google(audio)
				formatted_str = format(value).encode("utf-8")

				lang_check_blob = TextBlob(formatted_str)
				language = lang_check_blob.detect_language()
				print "checking for spanish"
				if format(language).encode("utf-8") == 'es':
					print(u"You said " + formatted_str)
					if formatted_str == "s*":
						formatted_str = "I am Lingobot and you? "
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)
						with m as source: audio = r.listen(source)
						print("Got it! Now to recognize it...")
						value = r.recognize_google(audio)
						formatted_str = format(value).encode("utf-8")

						tr_blob = TextBlob(formatted_str)
						tr_string = tr_blob.translate(to='en')
						speaker.say("You said " + str(tr_string) + " in spanish")
						speaker.runAndWait()


						formatted_str = "Hmm ! Where are you from?"
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)
						with m as source: audio = r.listen(source)
						print("Got it! Now to recognize it...")
						value = r.recognize_google(audio)
						formatted_str = format(value).encode("utf-8")

						tr_blob = TextBlob(formatted_str)
						tr_string = tr_blob.translate(to='en')
						speaker.say("You said " + str(tr_string) + " in spanish")
						speaker.runAndWait()


						formatted_str = "How old are you? "
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)
						with m as source: audio = r.listen(source)
						print("Got it! Now to recognize it...")
						value = r.recognize_google(audio)
						formatted_str = format(value).encode("utf-8")

						tr_blob = TextBlob(formatted_str)
						tr_string = tr_blob.translate(to='en')
						speaker.say("You said " + str(tr_string) + " in spanish")
						speaker.runAndWait()



						formatted_str = "When is your birthday? "
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)
						with m as source: audio = r.listen(source)
						print("Got it! Now to recognize it...")
						value = r.recognize_google(audio)
						formatted_str = format(value).encode("utf-8")

						tr_blob = TextBlob(formatted_str)
						tr_string = tr_blob.translate(to='en')
						speaker.say("You said " + str(tr_string) + " in spanish")
						speaker.runAndWait()




						formatted_str = "can you tell me the capital of spain?"
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)
						with m as source: audio = r.listen(source)
						print("Got it! Now to recognize it...")
						value = r.recognize_google(audio)
						formatted_str = format(value).encode("utf-8")

						tr_blob = TextBlob(formatted_str)
						tr_string = tr_blob.translate(to='en')
						speaker.say("You said " + str(tr_string) + " in spanish")
						speaker.runAndWait()


						if formatted_str=="Madrid":
							formatted_str = "wow good"
							in_string = tr_blob.translate(to='es')
							speaker.say(in_string)
						else:
							formatted_str = "nevermind! it is madrid"
							in_string = tr_blob.translate(to='es')
							speaker.say(in_string)




						formatted_str = "ok say something in spanish and i'll translate in english"
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)
						for i in range(0,5):
							with m as source: audio = r.listen(source)
							print("Got it! Now to recognize it...")
							value = r.recognize_google(audio)
							formatted_str = format(value).encode("utf-8")

							tr_blob = TextBlob(formatted_str)
							tr_string = tr_blob.translate(to='en')
							speaker.say("You said " + str(tr_string) + " in spanish")
							speaker.runAndWait()
							formatted_str = "want more?"
							in_string = tr_blob.translate(to='es')
							speaker.say(in_string)
							with m as source: audio = r.listen(source)
							print("Got it! Now to recognize it...")
							value = r.recognize_google(audio)
							formatted_str = format(value).encode("utf-8")
							if formatted_str=="no":
								break


						formatted_str = "Ok then,good bye! see you soon "
						in_string = tr_blob.translate(to='es')
						speaker.say(in_string)


				elif formatted_str == "no":
					formatted_str = "Ok then,good bye! see you soon "
					in_string = tr_blob.translate(to='es')
					speaker.say(in_string)



					#tr_blob = TextBlob(formatted_str)
					#tr_string = tr_blob.translate(to='en')
					#speaker.say("You said " + str(tr_string) + " in english")
					speaker.runAndWait()
			else: # this version of Python uses unicode for strings (Python 3+)
				print("You said {}".format(value))
		except sr.UnknownValueError:
			print("Oops! Didn't catch that")
		except sr.RequestError as e:
			print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
	pass
