package eventb2python.PyAST_Expressions;

public class PyAST_AtomicExpression extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String AtomicExpression;
	public String AtomicExpressionTranslation;
	public String PreludeName;
	
	//Constructor
	public PyAST_AtomicExpression(String atomicExpression){
		CoreExpression = "AtomicExpression";
		AtomicExpression = atomicExpression;
		PreludeName = "P";
		
		switch(atomicExpression) {
		case "Bool":
			AtomicExpressionTranslation = PreludeName + ".BOOL()";
			break;
		case "True":
			AtomicExpressionTranslation = "True";
			break;
		case "False":
			AtomicExpressionTranslation = "False";
			break;
		case "Integer":
			AtomicExpressionTranslation = PreludeName + ".INT()";
			break;
		case "Natural":
			AtomicExpressionTranslation = PreludeName + ".NAT()";
			break;
		case "Natural1":
			AtomicExpressionTranslation = PreludeName + ".NAT1()";
			break;
		case "EmptySet":
			AtomicExpressionTranslation = "PySet()";
			break;
		case "ID":
			AtomicExpressionTranslation = PreludeName + ".ID()";
			break;
		default:
			AtomicExpressionTranslation = " ErrorPyAST_AtomicExpression ";
		}
	}
}
