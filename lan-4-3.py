<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lan-4-3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2026-07-06 09:13:37 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0wNjswODo1MzoxMyBBTTsyNzQz"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0wNjswOToxMzozNyBBTTsxOzI4NTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="hours" type="Real" array="False" size=""/>
            <input variable="hours"/>
            <declare name="fee" type="Integer" array="False" size=""/>
            <if expression="hours &lt;= 2">
                <then>
                    <assign variable="fee" expression="0"/>
                </then>
                <else>
                    <if expression="hours &lt;= 5">
                        <then>
                            <assign variable="fee" expression="2"/>
                        </then>
                        <else>
                            <assign variable="fee" expression="3"/>
                        </else>
                    </if>
                </else>
            </if>
            <declare name="parkingFee" type="Real" array="False" size=""/>
            <assign variable="parkingFee" expression="hours*fee"/>
            <if expression="parkingFee &gt;= 30">
                <then>
                    <assign variable="parkingFee" expression="30"/>
                </then>
                <else/>
            </if>
            <output expression="parkingFee" newline="True"/>
        </body>
    </function>
</flowgorithm>
