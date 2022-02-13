def det_theft(sensor_reading, clf):

  prob = clf.predict_proba(sensor_reading)
  match = 0
  for i in prob:
    for o in i:
      if o > 0.8:
        driver = clf.predict(sensor_reading)
        print("You are driver #: ")
        print(driver)
        match = 1

  if match == 0:
        print("theft detected")
        
