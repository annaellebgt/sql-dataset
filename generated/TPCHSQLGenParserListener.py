# Generated from TPCHSQLGenParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TPCHSQLGenParser import TPCHSQLGenParser
else:
    from TPCHSQLGenParser import TPCHSQLGenParser

# This class defines a complete listener for a parse tree produced by TPCHSQLGenParser.
class TPCHSQLGenParserListener(ParseTreeListener):

    # Enter a parse tree produced by TPCHSQLGenParser#start_statement.
    def enterStart_statement(self, ctx:TPCHSQLGenParser.Start_statementContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#start_statement.
    def exitStart_statement(self, ctx:TPCHSQLGenParser.Start_statementContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#select_statement.
    def enterSelect_statement(self, ctx:TPCHSQLGenParser.Select_statementContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#select_statement.
    def exitSelect_statement(self, ctx:TPCHSQLGenParser.Select_statementContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#with_statment.
    def enterWith_statment(self, ctx:TPCHSQLGenParser.With_statmentContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#with_statment.
    def exitWith_statment(self, ctx:TPCHSQLGenParser.With_statmentContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#from_list.
    def enterFrom_list(self, ctx:TPCHSQLGenParser.From_listContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#from_list.
    def exitFrom_list(self, ctx:TPCHSQLGenParser.From_listContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#table_ref.
    def enterTable_ref(self, ctx:TPCHSQLGenParser.Table_refContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#table_ref.
    def exitTable_ref(self, ctx:TPCHSQLGenParser.Table_refContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#column_list.
    def enterColumn_list(self, ctx:TPCHSQLGenParser.Column_listContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#column_list.
    def exitColumn_list(self, ctx:TPCHSQLGenParser.Column_listContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#columnref.
    def enterColumnref(self, ctx:TPCHSQLGenParser.ColumnrefContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#columnref.
    def exitColumnref(self, ctx:TPCHSQLGenParser.ColumnrefContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#c_expr.
    def enterC_expr(self, ctx:TPCHSQLGenParser.C_exprContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#c_expr.
    def exitC_expr(self, ctx:TPCHSQLGenParser.C_exprContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#f_expr.
    def enterF_expr(self, ctx:TPCHSQLGenParser.F_exprContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#f_expr.
    def exitF_expr(self, ctx:TPCHSQLGenParser.F_exprContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#typeidentifier.
    def enterTypeidentifier(self, ctx:TPCHSQLGenParser.TypeidentifierContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#typeidentifier.
    def exitTypeidentifier(self, ctx:TPCHSQLGenParser.TypeidentifierContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#group_clause.
    def enterGroup_clause(self, ctx:TPCHSQLGenParser.Group_clauseContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#group_clause.
    def exitGroup_clause(self, ctx:TPCHSQLGenParser.Group_clauseContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#group_by_list.
    def enterGroup_by_list(self, ctx:TPCHSQLGenParser.Group_by_listContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#group_by_list.
    def exitGroup_by_list(self, ctx:TPCHSQLGenParser.Group_by_listContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#having_clause.
    def enterHaving_clause(self, ctx:TPCHSQLGenParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#having_clause.
    def exitHaving_clause(self, ctx:TPCHSQLGenParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#sort_clause.
    def enterSort_clause(self, ctx:TPCHSQLGenParser.Sort_clauseContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#sort_clause.
    def exitSort_clause(self, ctx:TPCHSQLGenParser.Sort_clauseContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#sortby_list.
    def enterSortby_list(self, ctx:TPCHSQLGenParser.Sortby_listContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#sortby_list.
    def exitSortby_list(self, ctx:TPCHSQLGenParser.Sortby_listContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#sortby.
    def enterSortby(self, ctx:TPCHSQLGenParser.SortbyContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#sortby.
    def exitSortby(self, ctx:TPCHSQLGenParser.SortbyContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#join_clause.
    def enterJoin_clause(self, ctx:TPCHSQLGenParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#join_clause.
    def exitJoin_clause(self, ctx:TPCHSQLGenParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#collabel.
    def enterCollabel(self, ctx:TPCHSQLGenParser.CollabelContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#collabel.
    def exitCollabel(self, ctx:TPCHSQLGenParser.CollabelContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#binary_op.
    def enterBinary_op(self, ctx:TPCHSQLGenParser.Binary_opContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#binary_op.
    def exitBinary_op(self, ctx:TPCHSQLGenParser.Binary_opContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#unary_op.
    def enterUnary_op(self, ctx:TPCHSQLGenParser.Unary_opContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#unary_op.
    def exitUnary_op(self, ctx:TPCHSQLGenParser.Unary_opContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#limit_clause.
    def enterLimit_clause(self, ctx:TPCHSQLGenParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#limit_clause.
    def exitLimit_clause(self, ctx:TPCHSQLGenParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#create_table.
    def enterCreate_table(self, ctx:TPCHSQLGenParser.Create_tableContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#create_table.
    def exitCreate_table(self, ctx:TPCHSQLGenParser.Create_tableContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#tableNameRef.
    def enterTableNameRef(self, ctx:TPCHSQLGenParser.TableNameRefContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#tableNameRef.
    def exitTableNameRef(self, ctx:TPCHSQLGenParser.TableNameRefContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#columnDefinitions.
    def enterColumnDefinitions(self, ctx:TPCHSQLGenParser.ColumnDefinitionsContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#columnDefinitions.
    def exitColumnDefinitions(self, ctx:TPCHSQLGenParser.ColumnDefinitionsContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#columnDefinition.
    def enterColumnDefinition(self, ctx:TPCHSQLGenParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#columnDefinition.
    def exitColumnDefinition(self, ctx:TPCHSQLGenParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#columnNameRef.
    def enterColumnNameRef(self, ctx:TPCHSQLGenParser.ColumnNameRefContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#columnNameRef.
    def exitColumnNameRef(self, ctx:TPCHSQLGenParser.ColumnNameRefContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#dataType.
    def enterDataType(self, ctx:TPCHSQLGenParser.DataTypeContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#dataType.
    def exitDataType(self, ctx:TPCHSQLGenParser.DataTypeContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#columnConstraints.
    def enterColumnConstraints(self, ctx:TPCHSQLGenParser.ColumnConstraintsContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#columnConstraints.
    def exitColumnConstraints(self, ctx:TPCHSQLGenParser.ColumnConstraintsContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#constraintExpression.
    def enterConstraintExpression(self, ctx:TPCHSQLGenParser.ConstraintExpressionContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#constraintExpression.
    def exitConstraintExpression(self, ctx:TPCHSQLGenParser.ConstraintExpressionContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#value.
    def enterValue(self, ctx:TPCHSQLGenParser.ValueContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#value.
    def exitValue(self, ctx:TPCHSQLGenParser.ValueContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#constraints.
    def enterConstraints(self, ctx:TPCHSQLGenParser.ConstraintsContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#constraints.
    def exitConstraints(self, ctx:TPCHSQLGenParser.ConstraintsContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#foreignKeyConstraint.
    def enterForeignKeyConstraint(self, ctx:TPCHSQLGenParser.ForeignKeyConstraintContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#foreignKeyConstraint.
    def exitForeignKeyConstraint(self, ctx:TPCHSQLGenParser.ForeignKeyConstraintContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#primaryKeyConstraint.
    def enterPrimaryKeyConstraint(self, ctx:TPCHSQLGenParser.PrimaryKeyConstraintContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#primaryKeyConstraint.
    def exitPrimaryKeyConstraint(self, ctx:TPCHSQLGenParser.PrimaryKeyConstraintContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#primaryKeyName.
    def enterPrimaryKeyName(self, ctx:TPCHSQLGenParser.PrimaryKeyNameContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#primaryKeyName.
    def exitPrimaryKeyName(self, ctx:TPCHSQLGenParser.PrimaryKeyNameContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#checkConstraint.
    def enterCheckConstraint(self, ctx:TPCHSQLGenParser.CheckConstraintContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#checkConstraint.
    def exitCheckConstraint(self, ctx:TPCHSQLGenParser.CheckConstraintContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#checkName.
    def enterCheckName(self, ctx:TPCHSQLGenParser.CheckNameContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#checkName.
    def exitCheckName(self, ctx:TPCHSQLGenParser.CheckNameContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#uniqueConstraint.
    def enterUniqueConstraint(self, ctx:TPCHSQLGenParser.UniqueConstraintContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#uniqueConstraint.
    def exitUniqueConstraint(self, ctx:TPCHSQLGenParser.UniqueConstraintContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#uniqueName.
    def enterUniqueName(self, ctx:TPCHSQLGenParser.UniqueNameContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#uniqueName.
    def exitUniqueName(self, ctx:TPCHSQLGenParser.UniqueNameContext):
        pass


    # Enter a parse tree produced by TPCHSQLGenParser#foreignKeyName.
    def enterForeignKeyName(self, ctx:TPCHSQLGenParser.ForeignKeyNameContext):
        pass

    # Exit a parse tree produced by TPCHSQLGenParser#foreignKeyName.
    def exitForeignKeyName(self, ctx:TPCHSQLGenParser.ForeignKeyNameContext):
        pass



del TPCHSQLGenParser