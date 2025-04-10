# Generated from BasicSQLGenParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BasicSQLGenParser import BasicSQLGenParser
else:
    from generated.BasicSQLGenParser import BasicSQLGenParser

# This class defines a complete listener for a parse tree produced by BasicSQLGenParser.
class BasicSQLGenParserListener(ParseTreeListener):

    # Enter a parse tree produced by BasicSQLGenParser#select_statement.
    def enterSelect_statement(self, ctx:BasicSQLGenParser.Select_statementContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#select_statement.
    def exitSelect_statement(self, ctx:BasicSQLGenParser.Select_statementContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#from_list.
    def enterFrom_list(self, ctx:BasicSQLGenParser.From_listContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#from_list.
    def exitFrom_list(self, ctx:BasicSQLGenParser.From_listContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#table_ref.
    def enterTable_ref(self, ctx:BasicSQLGenParser.Table_refContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#table_ref.
    def exitTable_ref(self, ctx:BasicSQLGenParser.Table_refContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#c_expr.
    def enterC_expr(self, ctx:BasicSQLGenParser.C_exprContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#c_expr.
    def exitC_expr(self, ctx:BasicSQLGenParser.C_exprContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#columnref.
    def enterColumnref(self, ctx:BasicSQLGenParser.ColumnrefContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#columnref.
    def exitColumnref(self, ctx:BasicSQLGenParser.ColumnrefContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#group_clause.
    def enterGroup_clause(self, ctx:BasicSQLGenParser.Group_clauseContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#group_clause.
    def exitGroup_clause(self, ctx:BasicSQLGenParser.Group_clauseContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#group_by_list.
    def enterGroup_by_list(self, ctx:BasicSQLGenParser.Group_by_listContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#group_by_list.
    def exitGroup_by_list(self, ctx:BasicSQLGenParser.Group_by_listContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#having_clause.
    def enterHaving_clause(self, ctx:BasicSQLGenParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#having_clause.
    def exitHaving_clause(self, ctx:BasicSQLGenParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#sort_clause.
    def enterSort_clause(self, ctx:BasicSQLGenParser.Sort_clauseContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#sort_clause.
    def exitSort_clause(self, ctx:BasicSQLGenParser.Sort_clauseContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#column_list.
    def enterColumn_list(self, ctx:BasicSQLGenParser.Column_listContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#column_list.
    def exitColumn_list(self, ctx:BasicSQLGenParser.Column_listContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#sortby_list.
    def enterSortby_list(self, ctx:BasicSQLGenParser.Sortby_listContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#sortby_list.
    def exitSortby_list(self, ctx:BasicSQLGenParser.Sortby_listContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#sortby.
    def enterSortby(self, ctx:BasicSQLGenParser.SortbyContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#sortby.
    def exitSortby(self, ctx:BasicSQLGenParser.SortbyContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#collabel.
    def enterCollabel(self, ctx:BasicSQLGenParser.CollabelContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#collabel.
    def exitCollabel(self, ctx:BasicSQLGenParser.CollabelContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#binary_op.
    def enterBinary_op(self, ctx:BasicSQLGenParser.Binary_opContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#binary_op.
    def exitBinary_op(self, ctx:BasicSQLGenParser.Binary_opContext):
        pass


    # Enter a parse tree produced by BasicSQLGenParser#unary_op.
    def enterUnary_op(self, ctx:BasicSQLGenParser.Unary_opContext):
        pass

    # Exit a parse tree produced by BasicSQLGenParser#unary_op.
    def exitUnary_op(self, ctx:BasicSQLGenParser.Unary_opContext):
        pass



del BasicSQLGenParser