from front_end import ManagementApp

def main()->None: 
    window = ManagementApp('Sale and Purchase Management',"Products")
    window.mainloop()


if __name__ == "__main__":
    main()