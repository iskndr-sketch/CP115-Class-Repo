<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab-4-2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2026-07-06 09:21:34 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0wNjswOToxNzoxNiBBTTsyNzQ3"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0wNjswOToyMTozNCBBTTsxOzI4NTA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="income" type="Real" array="False" size=""/>
            <input variable="income"/>
            <declare name="tax" type="Integer" array="False" size=""/>
            <if expression="income &lt;=50000">
                <then>
                    <assign variable="tax" expression="0"/>
                </then>
                <else>
                    <if expression="income &lt;=100000">
                        <then>
                            <assign variable="tax" expression="0.01"/>
                        </then>
                        <else>
                            <assign variable="tax" expression="0.02"/>
                        </else>
                    </if>
                </else>
            </if>
            <declare name="totaltax" type="Integer" array="False" size=""/>
            <assign variable="totalTax" expression="income*tax"/>
            <output expression="toatalTax" newline="True"/>
        </body>
    </function>
</flowgorithm>
