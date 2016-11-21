# Generated from Cbalc.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CbalcParser import CbalcParser
else:
    from CbalcParser import CbalcParser

# This class defines a complete generic visitor for a parse tree produced by CbalcParser.

class CbalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CbalcParser#prog.
    def visitProg(self, ctx:CbalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#line.
    def visitLine(self, ctx:CbalcParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#mulstat.
    def visitMulstat(self, ctx:CbalcParser.MulstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#lavel_no1.
    def visitLavel_no1(self, ctx:CbalcParser.Lavel_no1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#assign.
    def visitAssign(self, ctx:CbalcParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#showme.
    def visitShowme(self, ctx:CbalcParser.ShowmeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#parens.
    def visitParens(self, ctx:CbalcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#string.
    def visitString(self, ctx:CbalcParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#MulDiv.
    def visitMulDiv(self, ctx:CbalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#AddSub.
    def visitAddSub(self, ctx:CbalcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#logicOperOr.
    def visitLogicOperOr(self, ctx:CbalcParser.LogicOperOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#CompOper2.
    def visitCompOper2(self, ctx:CbalcParser.CompOper2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#BitOper.
    def visitBitOper(self, ctx:CbalcParser.BitOperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#CompOper.
    def visitCompOper(self, ctx:CbalcParser.CompOperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#number.
    def visitNumber(self, ctx:CbalcParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#SingleOper.
    def visitSingleOper(self, ctx:CbalcParser.SingleOperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#logicOperAnd.
    def visitLogicOperAnd(self, ctx:CbalcParser.LogicOperAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#id.
    def visitId(self, ctx:CbalcParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CbalcParser#ShiftOper.
    def visitShiftOper(self, ctx:CbalcParser.ShiftOperContext):
        return self.visitChildren(ctx)



del CbalcParser