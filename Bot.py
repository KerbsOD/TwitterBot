from Funciones import Daily, answer, schedule, time

if __name__ == '__main__':  
    
    print("------------------------------> WELCOME TO THE DOLLAR SHOP <------------------------------")

    Daily()
    
    while True:
        schedule.run_pending()
        answer()
        time.sleep(5)
    