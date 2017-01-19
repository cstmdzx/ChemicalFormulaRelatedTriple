# ChemicalFormulaRelatedTriple

Generate triples about chemical formula, including 反应物 and 生成物

+ **ChemicalReaction** 没有处理好的全是unicode的反应方程式
+ **ChemicalReactionChinese** 处理过的，生成是中文的反应方程式
+ **ChemicalRelated.xlsx** 一开始的一次处理，里面是部分方程式的反应物，不太全
+ **EquationImageDownload.py** 从**chemistryKnowledgebaseOutput.xlsx**中读出方程式的url并且下载显示，下载的图片放在**temp.img**，然后再显示
+ **EquationRelatedReactant.xlsx** 包含了方程式的反应物以及生成物，还有一些其他的，都是为了保存原始数据新建的，另外生成物那张表里有些备注，还没解决
+ **Product.py** 本来准备用来写生成物的程序，但是好像没什么用，因为生成物都用手标了
+ **ProductTriple.py** 把手标的结果生成三元组
+ **Reactant.py** 反应物，这个写的比较复杂一点，计划是直接用以前导出来的export.nt来处理，读出里面的方程式，功能上应该是实现了，但是好像不全,还不太确定
+ **Reactant2.py** 反应物，这个直接读**ChemicalRelated.xlsx**,把方程式利用正则表达式分出反应物，生成三元组放到**EquationRelatedReactant.xlsx**里
+ **SumUp** 统计一下目前完成的指标
+ **chemistryKnowledgebaseOutput.xlsx** 从sys中导出来的知识库
+ **test.py** just a test
