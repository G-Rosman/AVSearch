# Generated from ANTLR_PRO.g4 by ANTLR 4.13.1
from antlr4 import *
import re
if "." in __name__:
    from .ANTLR_PROParser import ANTLR_PROParser
else:
    from ANTLR_PROParser import ANTLR_PROParser

class ANTLR_PROVisitor(ParseTreeVisitor):
    file_path = ''
    def add_comment_to_file(self, search_text, comment_text):
        with open(self.file_path, 'r') as file:
            content = file.read()
        search_pattern = ''.join([f'{char}'+ r"\s*\n" for char in re.escape(search_text)])

    # Ищем исходный текст в файле, используя шаблон поиска
        match = re.search(search_pattern, content)
        if match:
            start_pos = match.start()
            prev_line_start = content.rfind('\n', 0, start_pos)
            if prev_line_start == -1:
                prev_line_start = 0
            new_content = content[:prev_line_start] + comment_text + '\n' + content[prev_line_start:]
            with open(self.file_path, 'w') as file:
                file.write(new_content)
            print(f"Комментарий {comment_text} успешно добавлен в файл.")
        else:
            pass
            #print("Исходный текст не найден в файле.")



    # Visit a parse tree produced by ANTLR_PROParser#translationUnit.
    def visitTranslationUnit(self, ctx:ANTLR_PROParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:ANTLR_PROParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#idExpression.
    def visitIdExpression(self, ctx:ANTLR_PROParser.IdExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#unqualifiedId.
    def visitUnqualifiedId(self, ctx:ANTLR_PROParser.UnqualifiedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#qualifiedId.
    def visitQualifiedId(self, ctx:ANTLR_PROParser.QualifiedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#nestedNameSpecifier.
    def visitNestedNameSpecifier(self, ctx:ANTLR_PROParser.NestedNameSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:ANTLR_PROParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#lambdaIntroducer.
    def visitLambdaIntroducer(self, ctx:ANTLR_PROParser.LambdaIntroducerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#lambdaCapture.
    def visitLambdaCapture(self, ctx:ANTLR_PROParser.LambdaCaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#captureDefault.
    def visitCaptureDefault(self, ctx:ANTLR_PROParser.CaptureDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#captureList.
    def visitCaptureList(self, ctx:ANTLR_PROParser.CaptureListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#capture.
    def visitCapture(self, ctx:ANTLR_PROParser.CaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#simpleCapture.
    def visitSimpleCapture(self, ctx:ANTLR_PROParser.SimpleCaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#initcapture.
    def visitInitcapture(self, ctx:ANTLR_PROParser.InitcaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#lambdaDeclarator.
    def visitLambdaDeclarator(self, ctx:ANTLR_PROParser.LambdaDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#postfixExpression.
    def visitPostfixExpression(self, ctx:ANTLR_PROParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typeIdOfTheTypeId.
    def visitTypeIdOfTheTypeId(self, ctx:ANTLR_PROParser.TypeIdOfTheTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#expressionList.
    def visitExpressionList(self, ctx:ANTLR_PROParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#pseudoDestructorName.
    def visitPseudoDestructorName(self, ctx:ANTLR_PROParser.PseudoDestructorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#unaryExpression.
    def visitUnaryExpression(self, ctx:ANTLR_PROParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#unaryOperator.
    def visitUnaryOperator(self, ctx:ANTLR_PROParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#newExpression_.
    def visitNewExpression_(self, ctx:ANTLR_PROParser.NewExpression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#newPlacement.
    def visitNewPlacement(self, ctx:ANTLR_PROParser.NewPlacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#newTypeId.
    def visitNewTypeId(self, ctx:ANTLR_PROParser.NewTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#newDeclarator_.
    def visitNewDeclarator_(self, ctx:ANTLR_PROParser.NewDeclarator_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#noPointerNewDeclarator.
    def visitNoPointerNewDeclarator(self, ctx:ANTLR_PROParser.NoPointerNewDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#newInitializer_.
    def visitNewInitializer_(self, ctx:ANTLR_PROParser.NewInitializer_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#deleteExpression.
    def visitDeleteExpression(self, ctx:ANTLR_PROParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#noExceptExpression.
    def visitNoExceptExpression(self, ctx:ANTLR_PROParser.NoExceptExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#castExpression.
    def visitCastExpression(self, ctx:ANTLR_PROParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#pointerMemberExpression.
    def visitPointerMemberExpression(self, ctx:ANTLR_PROParser.PointerMemberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:ANTLR_PROParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:ANTLR_PROParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#shiftExpression.
    def visitShiftExpression(self, ctx:ANTLR_PROParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#shiftOperator.
    def visitShiftOperator(self, ctx:ANTLR_PROParser.ShiftOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#relationalExpression.
    def visitRelationalExpression(self, ctx:ANTLR_PROParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#equalityExpression.
    def visitEqualityExpression(self, ctx:ANTLR_PROParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#andExpression.
    def visitAndExpression(self, ctx:ANTLR_PROParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:ANTLR_PROParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:ANTLR_PROParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:ANTLR_PROParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:ANTLR_PROParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:ANTLR_PROParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:ANTLR_PROParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ANTLR_PROParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#expression.
    def visitExpression(self, ctx:ANTLR_PROParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#constantExpression.
    def visitConstantExpression(self, ctx:ANTLR_PROParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#statement.
    def visitStatement(self, ctx:ANTLR_PROParser.StatementContext):
        text = ctx.getText()
        self.visitChildren(ctx)
        return text


    # Visit a parse tree produced by ANTLR_PROParser#labeledStatement.
    def visitLabeledStatement(self, ctx:ANTLR_PROParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#expressionStatement.
    def visitExpressionStatement(self, ctx:ANTLR_PROParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#compoundStatement.
    def visitCompoundStatement(self, ctx:ANTLR_PROParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#statementSeq.
    def visitStatementSeq(self, ctx:ANTLR_PROParser.StatementSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#selectionStatement.
    def visitSelectionStatement(self, ctx:ANTLR_PROParser.SelectionStatementContext):
        #self.add_comment_to_file(ctx.getText(), '// Блок IF')
        if ctx.getChildCount() == 5:
            print(ctx.getChild(0).getText(),end = ' ')
            print((ctx.getChild(1).getText()),end = ' ')
            cond = self.visit(ctx.condition())
            print(cond, end = ' ')
            print(ctx.getChild(3).getText(),end = ' ')
            statement = self.visit(ctx.statement(0)) 
            if "if" in statement[0:3]:
                print("Вложенный if")
            print(statement)
        if ctx.getChildCount() == 7:
            print(ctx.getChild(0).getText(),end = ' ')
            print((ctx.getChild(1).getText()),end = ' ')
            cond = self.visit(ctx.condition())
            print(cond,end = ' ')
            print(ctx.getChild(3).getText(),end = ' ')
            statement = self.visit(ctx.statement(0)) 
            if "if" in statement[0:3]:
                print("Вложенный if")
            print(statement, end = ' ')

            print(ctx.getChild(5).getText(),end = ' ')
            statement = self.visit(ctx.statement(1)) 
            if "if" in statement[0:3]:
                print("Вложенный if")
            print(statement)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#condition.
    def visitCondition(self, ctx:ANTLR_PROParser.ConditionContext):
        text = ctx.getText()
        self.visitChildren(ctx)
        return text


    # Visit a parse tree produced by ANTLR_PROParser#iterationStatement.
    def visitIterationStatement(self, ctx:ANTLR_PROParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#forInitStatement.
    def visitForInitStatement(self, ctx:ANTLR_PROParser.ForInitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#forRangeDeclaration.
    def visitForRangeDeclaration(self, ctx:ANTLR_PROParser.ForRangeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#forRangeInitializer.
    def visitForRangeInitializer(self, ctx:ANTLR_PROParser.ForRangeInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#jumpStatement.
    def visitJumpStatement(self, ctx:ANTLR_PROParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:ANTLR_PROParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declarationseq.
    def visitDeclarationseq(self, ctx:ANTLR_PROParser.DeclarationseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declaration.
    def visitDeclaration(self, ctx:ANTLR_PROParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#blockDeclaration.
    def visitBlockDeclaration(self, ctx:ANTLR_PROParser.BlockDeclarationContext):
        text = ctx.getText()
        self.visitChildren(ctx)
        return text


    # Visit a parse tree produced by ANTLR_PROParser#aliasDeclaration.
    def visitAliasDeclaration(self, ctx:ANTLR_PROParser.AliasDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#simpleDeclaration.
    def visitSimpleDeclaration(self, ctx:ANTLR_PROParser.SimpleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:ANTLR_PROParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#emptyDeclaration_.
    def visitEmptyDeclaration_(self, ctx:ANTLR_PROParser.EmptyDeclaration_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:ANTLR_PROParser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declSpecifier.
    def visitDeclSpecifier(self, ctx:ANTLR_PROParser.DeclSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declSpecifierSeq.
    def visitDeclSpecifierSeq(self, ctx:ANTLR_PROParser.DeclSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:ANTLR_PROParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:ANTLR_PROParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typedefName.
    def visitTypedefName(self, ctx:ANTLR_PROParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:ANTLR_PROParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#trailingTypeSpecifier.
    def visitTrailingTypeSpecifier(self, ctx:ANTLR_PROParser.TrailingTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typeSpecifierSeq.
    def visitTypeSpecifierSeq(self, ctx:ANTLR_PROParser.TypeSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#trailingTypeSpecifierSeq.
    def visitTrailingTypeSpecifierSeq(self, ctx:ANTLR_PROParser.TrailingTypeSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#simpleTypeLengthModifier.
    def visitSimpleTypeLengthModifier(self, ctx:ANTLR_PROParser.SimpleTypeLengthModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#simpleTypeSignednessModifier.
    def visitSimpleTypeSignednessModifier(self, ctx:ANTLR_PROParser.SimpleTypeSignednessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#simpleTypeSpecifier.
    def visitSimpleTypeSpecifier(self, ctx:ANTLR_PROParser.SimpleTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#theTypeName.
    def visitTheTypeName(self, ctx:ANTLR_PROParser.TheTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#decltypeSpecifier.
    def visitDecltypeSpecifier(self, ctx:ANTLR_PROParser.DecltypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#elaboratedTypeSpecifier.
    def visitElaboratedTypeSpecifier(self, ctx:ANTLR_PROParser.ElaboratedTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumName.
    def visitEnumName(self, ctx:ANTLR_PROParser.EnumNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:ANTLR_PROParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumHead.
    def visitEnumHead(self, ctx:ANTLR_PROParser.EnumHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#opaqueEnumDeclaration.
    def visitOpaqueEnumDeclaration(self, ctx:ANTLR_PROParser.OpaqueEnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumkey.
    def visitEnumkey(self, ctx:ANTLR_PROParser.EnumkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumbase.
    def visitEnumbase(self, ctx:ANTLR_PROParser.EnumbaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumeratorList.
    def visitEnumeratorList(self, ctx:ANTLR_PROParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumeratorDefinition.
    def visitEnumeratorDefinition(self, ctx:ANTLR_PROParser.EnumeratorDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#enumerator.
    def visitEnumerator(self, ctx:ANTLR_PROParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#namespaceName.
    def visitNamespaceName(self, ctx:ANTLR_PROParser.NamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#originalNamespaceName.
    def visitOriginalNamespaceName(self, ctx:ANTLR_PROParser.OriginalNamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#namespaceDefinition.
    def visitNamespaceDefinition(self, ctx:ANTLR_PROParser.NamespaceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#namespaceAlias.
    def visitNamespaceAlias(self, ctx:ANTLR_PROParser.NamespaceAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#namespaceAliasDefinition.
    def visitNamespaceAliasDefinition(self, ctx:ANTLR_PROParser.NamespaceAliasDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#qualifiednamespacespecifier.
    def visitQualifiednamespacespecifier(self, ctx:ANTLR_PROParser.QualifiednamespacespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#usingDeclaration.
    def visitUsingDeclaration(self, ctx:ANTLR_PROParser.UsingDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#usingDirective.
    def visitUsingDirective(self, ctx:ANTLR_PROParser.UsingDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#asmDefinition.
    def visitAsmDefinition(self, ctx:ANTLR_PROParser.AsmDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#linkageSpecification.
    def visitLinkageSpecification(self, ctx:ANTLR_PROParser.LinkageSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attributeSpecifierSeq.
    def visitAttributeSpecifierSeq(self, ctx:ANTLR_PROParser.AttributeSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attributeSpecifier.
    def visitAttributeSpecifier(self, ctx:ANTLR_PROParser.AttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#alignmentspecifier.
    def visitAlignmentspecifier(self, ctx:ANTLR_PROParser.AlignmentspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attributeList.
    def visitAttributeList(self, ctx:ANTLR_PROParser.AttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attribute.
    def visitAttribute(self, ctx:ANTLR_PROParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attributeNamespace.
    def visitAttributeNamespace(self, ctx:ANTLR_PROParser.AttributeNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#attributeArgumentClause.
    def visitAttributeArgumentClause(self, ctx:ANTLR_PROParser.AttributeArgumentClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#balancedTokenSeq.
    def visitBalancedTokenSeq(self, ctx:ANTLR_PROParser.BalancedTokenSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#balancedtoken.
    def visitBalancedtoken(self, ctx:ANTLR_PROParser.BalancedtokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:ANTLR_PROParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#initDeclarator.
    def visitInitDeclarator(self, ctx:ANTLR_PROParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declarator.
    def visitDeclarator(self, ctx:ANTLR_PROParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#pointerDeclarator.
    def visitPointerDeclarator(self, ctx:ANTLR_PROParser.PointerDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#noPointerDeclarator.
    def visitNoPointerDeclarator(self, ctx:ANTLR_PROParser.NoPointerDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#parametersAndQualifiers.
    def visitParametersAndQualifiers(self, ctx:ANTLR_PROParser.ParametersAndQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#trailingReturnType.
    def visitTrailingReturnType(self, ctx:ANTLR_PROParser.TrailingReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#pointerOperator.
    def visitPointerOperator(self, ctx:ANTLR_PROParser.PointerOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#cvqualifierseq.
    def visitCvqualifierseq(self, ctx:ANTLR_PROParser.CvqualifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#cvQualifier.
    def visitCvQualifier(self, ctx:ANTLR_PROParser.CvQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#refqualifier.
    def visitRefqualifier(self, ctx:ANTLR_PROParser.RefqualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#declaratorid.
    def visitDeclaratorid(self, ctx:ANTLR_PROParser.DeclaratoridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#theTypeId.
    def visitTheTypeId(self, ctx:ANTLR_PROParser.TheTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:ANTLR_PROParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#pointerAbstractDeclarator.
    def visitPointerAbstractDeclarator(self, ctx:ANTLR_PROParser.PointerAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#noPointerAbstractDeclarator.
    def visitNoPointerAbstractDeclarator(self, ctx:ANTLR_PROParser.NoPointerAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#abstractPackDeclarator.
    def visitAbstractPackDeclarator(self, ctx:ANTLR_PROParser.AbstractPackDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#noPointerAbstractPackDeclarator.
    def visitNoPointerAbstractPackDeclarator(self, ctx:ANTLR_PROParser.NoPointerAbstractPackDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#parameterDeclarationClause.
    def visitParameterDeclarationClause(self, ctx:ANTLR_PROParser.ParameterDeclarationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#parameterDeclarationList.
    def visitParameterDeclarationList(self, ctx:ANTLR_PROParser.ParameterDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:ANTLR_PROParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:ANTLR_PROParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#functionBody.
    def visitFunctionBody(self, ctx:ANTLR_PROParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#initializer.
    def visitInitializer(self, ctx:ANTLR_PROParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#braceOrEqualInitializer.
    def visitBraceOrEqualInitializer(self, ctx:ANTLR_PROParser.BraceOrEqualInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#initializerClause.
    def visitInitializerClause(self, ctx:ANTLR_PROParser.InitializerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#initializerList.
    def visitInitializerList(self, ctx:ANTLR_PROParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#bracedInitList.
    def visitBracedInitList(self, ctx:ANTLR_PROParser.BracedInitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#className.
    def visitClassName(self, ctx:ANTLR_PROParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#classSpecifier.
    def visitClassSpecifier(self, ctx:ANTLR_PROParser.ClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#classHead.
    def visitClassHead(self, ctx:ANTLR_PROParser.ClassHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#classHeadName.
    def visitClassHeadName(self, ctx:ANTLR_PROParser.ClassHeadNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#classVirtSpecifier.
    def visitClassVirtSpecifier(self, ctx:ANTLR_PROParser.ClassVirtSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#classKey.
    def visitClassKey(self, ctx:ANTLR_PROParser.ClassKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#memberSpecification.
    def visitMemberSpecification(self, ctx:ANTLR_PROParser.MemberSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#memberdeclaration.
    def visitMemberdeclaration(self, ctx:ANTLR_PROParser.MemberdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#memberDeclaratorList.
    def visitMemberDeclaratorList(self, ctx:ANTLR_PROParser.MemberDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#memberDeclarator.
    def visitMemberDeclarator(self, ctx:ANTLR_PROParser.MemberDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#virtualSpecifierSeq.
    def visitVirtualSpecifierSeq(self, ctx:ANTLR_PROParser.VirtualSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#virtualSpecifier.
    def visitVirtualSpecifier(self, ctx:ANTLR_PROParser.VirtualSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#pureSpecifier.
    def visitPureSpecifier(self, ctx:ANTLR_PROParser.PureSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#baseClause.
    def visitBaseClause(self, ctx:ANTLR_PROParser.BaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#baseSpecifierList.
    def visitBaseSpecifierList(self, ctx:ANTLR_PROParser.BaseSpecifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#baseSpecifier.
    def visitBaseSpecifier(self, ctx:ANTLR_PROParser.BaseSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#classOrDeclType.
    def visitClassOrDeclType(self, ctx:ANTLR_PROParser.ClassOrDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#baseTypeSpecifier.
    def visitBaseTypeSpecifier(self, ctx:ANTLR_PROParser.BaseTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:ANTLR_PROParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#conversionFunctionId.
    def visitConversionFunctionId(self, ctx:ANTLR_PROParser.ConversionFunctionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#conversionTypeId.
    def visitConversionTypeId(self, ctx:ANTLR_PROParser.ConversionTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#conversionDeclarator.
    def visitConversionDeclarator(self, ctx:ANTLR_PROParser.ConversionDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#constructorInitializer.
    def visitConstructorInitializer(self, ctx:ANTLR_PROParser.ConstructorInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#memInitializerList.
    def visitMemInitializerList(self, ctx:ANTLR_PROParser.MemInitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#memInitializer.
    def visitMemInitializer(self, ctx:ANTLR_PROParser.MemInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#meminitializerid.
    def visitMeminitializerid(self, ctx:ANTLR_PROParser.MeminitializeridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#operatorFunctionId.
    def visitOperatorFunctionId(self, ctx:ANTLR_PROParser.OperatorFunctionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#literalOperatorId.
    def visitLiteralOperatorId(self, ctx:ANTLR_PROParser.LiteralOperatorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateDeclaration.
    def visitTemplateDeclaration(self, ctx:ANTLR_PROParser.TemplateDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateparameterList.
    def visitTemplateparameterList(self, ctx:ANTLR_PROParser.TemplateparameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateParameter.
    def visitTemplateParameter(self, ctx:ANTLR_PROParser.TemplateParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typeParameter.
    def visitTypeParameter(self, ctx:ANTLR_PROParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#simpleTemplateId.
    def visitSimpleTemplateId(self, ctx:ANTLR_PROParser.SimpleTemplateIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateId.
    def visitTemplateId(self, ctx:ANTLR_PROParser.TemplateIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateName.
    def visitTemplateName(self, ctx:ANTLR_PROParser.TemplateNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateArgumentList.
    def visitTemplateArgumentList(self, ctx:ANTLR_PROParser.TemplateArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#templateArgument.
    def visitTemplateArgument(self, ctx:ANTLR_PROParser.TemplateArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typeNameSpecifier.
    def visitTypeNameSpecifier(self, ctx:ANTLR_PROParser.TypeNameSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#explicitInstantiation.
    def visitExplicitInstantiation(self, ctx:ANTLR_PROParser.ExplicitInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#explicitSpecialization.
    def visitExplicitSpecialization(self, ctx:ANTLR_PROParser.ExplicitSpecializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#tryBlock.
    def visitTryBlock(self, ctx:ANTLR_PROParser.TryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#functionTryBlock.
    def visitFunctionTryBlock(self, ctx:ANTLR_PROParser.FunctionTryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#handlerSeq.
    def visitHandlerSeq(self, ctx:ANTLR_PROParser.HandlerSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#handler.
    def visitHandler(self, ctx:ANTLR_PROParser.HandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#exceptionDeclaration.
    def visitExceptionDeclaration(self, ctx:ANTLR_PROParser.ExceptionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#throwExpression.
    def visitThrowExpression(self, ctx:ANTLR_PROParser.ThrowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#exceptionSpecification.
    def visitExceptionSpecification(self, ctx:ANTLR_PROParser.ExceptionSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#dynamicExceptionSpecification.
    def visitDynamicExceptionSpecification(self, ctx:ANTLR_PROParser.DynamicExceptionSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#typeIdList.
    def visitTypeIdList(self, ctx:ANTLR_PROParser.TypeIdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#noeExceptSpecification.
    def visitNoeExceptSpecification(self, ctx:ANTLR_PROParser.NoeExceptSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#theOperator.
    def visitTheOperator(self, ctx:ANTLR_PROParser.TheOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR_PROParser#literal.
    def visitLiteral(self, ctx:ANTLR_PROParser.LiteralContext):
        return self.visitChildren(ctx)



del ANTLR_PROParser