{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def longestCommonPrefix(self, myArr):\
        prefix = myArr[0]\
        print(prefix)\
        myResult = ""\
        nn = len(prefix)\
        if myArr == "":\
            return \
        #str1 = myArr[0]\
        str2 = myArr[1]\
        str3 = myArr[2]\
        \
        for i in str2[0:]:\
            print(i)\
            \
            while i.startswith(nn(i)):\
                print(prefix[:1])\
                print(i.startswith(prefix[:1]))\
                \
                \
               \
                myResult += i\
                #prefix = prefix[:1]\
                nn += 1\
            \
        return prefix    \
myVar = Solution()\
myVar.longestCommonPrefix(["flower","flow","flight"])}