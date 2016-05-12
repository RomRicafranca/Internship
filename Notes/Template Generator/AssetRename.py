file = open("Expenses.txt")

idtitle = 729
for line in file:
    line = line.split(":: ")
    print("""        <record model="account.account.template" id="account_account_""" + str(idtitle) + """">
            <field name="name">""" + str(line[1]).rstrip() + """</field>
            <field name="code">""" + str(line[0]) + """</field>
            <field name="user_type_id" ref="account.data_account_type_expenses" />
            <field name="chart_template_id" ref="ph_chart_template"/>
            <field name="reconcile" eval="False" />
        </record>""", end="\n\n")
    
    idtitle = idtitle + 1;
