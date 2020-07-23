package eventb2python.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.handlers.HandlerUtil;
import org.rodinp.core.RodinDBException;
import org.eclipse.jface.dialogs.MessageDialog;

public class SampleHandler extends AbstractHandler {
	//Public Attributes
	public EB2PY Translator;
	
	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		
		//Create Translator Instance.
		try {
			Translator = new EB2PY();
		} catch (RodinDBException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if(!Translator.AvailableProjects) {
			IWorkbenchWindow window = HandlerUtil.getActiveWorkbenchWindowChecked(event);
			MessagePopUp(window,"There are no projects to translate!");
			return null;
		}
		
		try {
			Translator.TranslateProjects();
		} catch (RodinDBException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		//Activation of the button (and PopUp message) - End of the main execute method.
		IWorkbenchWindow window = HandlerUtil.getActiveWorkbenchWindowChecked(event);
		MessagePopUp(window,"Check the Translations Folder named 'Output_EB2PY'!");
		return null;
	}
	
	//Display PopUp Message when the EB2PY button is clicked.
	public void MessagePopUp(IWorkbenchWindow window,String message) {
		MessageDialog.openInformation(
				window.getShell(),
				"EventB2Python",
				message);
	}
}
