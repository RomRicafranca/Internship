def generate(file, xmlgen):
    idcount = 696 #Counter
    
    for line in file:
        line = line.split(":: ")
        
        if(line[2] == "1"):
            user_type_id = "account.data_account_type_current_assets"
        elif(line[2] == "2"):
            user_type_id = "account.data_account_type_current_liabilities"
        elif(line[2] == "3"):
            user_type_id = "account.data_account_type_equity"
        elif(line[2] == "4"):
            user_type_id = "account.data_account_type_revenue"
        else:
            user_type_id = "account.data_account_type_expenses"
                        
        xmlgen.write("""\n\n\t<record model="account.account.template" id="account_account_""" + str(idcount) + """">
\t\t<field name="name">""" + str(line[1]).rstrip() + """</field> """ #Field name
                + """\n\t\t<field name="code">""" + str(line[0]) + """</field> """ #Field code
                + """\n\t\t<field name="user_type_id" ref=\""""+ user_type_id +"""" />
\t\t<field name="chart_template_id" ref="ph_chart_template"/>
\t\t<field name="reconcile" eval="False" />
\t</record>""")
        
        idcount = idcount + 1;


if __name__ == "__main__":
        
        datalist = []
        
        xmlgen = open('chart.xml','w+') #Creates a chart.xml file, and writes to it

        xmlgen.write('''<<?xml version="1.0" encoding="utf-8"?>\n<odoo>''') #writes opening tags
        
        file = open("Data\Assets.txt") #Opens Assets
        
        for line in file:
                datalist.append(line + ":: 1") #Reads the file, adds it to data list, and adding extra data to distinguish it as an asset
                
        file = open("Data\Liabilities.txt") #Opens Liabilities
        
        for line in file:
                datalist.append(line + ":: 2") #Reads the file, adds it to data list, and adding extra data to distinguish it as a liability
                
        file = open("Data\Equities.txt")

        for line in file:
                datalist.append(line + ":: 3") #Reads the file, adds it to data list, and adding extra data to distinguish it as equity

        file = open("Data\Income.txt")

        for line in file:
                datalist.append(line + ":: 4") #Reads the file, adds it to data list, and adding extra data to distinguish it as income

        file = open("Data\Expenses.txt")
        
        for line in file:
                datalist.append(line + ":: 5") #Reads the file, adds it to data list, and adding extra data to distinguish it as expenses
        
        file = None
        
        generate(datalist, xmlgen) 

        xmlgen.write("\n\n</odoo>") #closes odoo tag from beginning
        xmlgen.close() 
