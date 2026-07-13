<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab-4-2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2026-07-13 08:39:13 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0wNjswOToxNzoxNiBBTTsyNzQ3"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0xMzswODozOToxMyBBTTs0OzI4NTY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="income" type="Real" array="False" size=""/>
            <declare name="totalTax" type="Integer" array="False" size=""/>
            <input variable="income"/>
            <if expression="income &lt;=50000">
                <then>
                    <assign variable="totalTax" expression="0"/>
                </then>
                <else>
                    <if expression="income &gt;=100000">
                        <then>
                            <assign variable="totalTax" expression="(income-100000)*0.02+(50000*0.01)"/>
                        </then>
                        <else>
                            <assign variable="totalTax" expression="(income-50000)*0.01"/>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="totalTax" newline="True"/>
        </body>
    </function>
</flowgorithm>
