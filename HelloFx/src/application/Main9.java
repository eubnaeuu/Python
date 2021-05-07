package application;
	
import java.io.IOException;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.Event;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main9 extends Application {
	TextField tf;
	@Override
	public void start(Stage primaryStage) {
		AnchorPane root;
		try {
			root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main9.fxml"));
			primaryStage.setTitle("Application"); 
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			
			Button btn0 = (Button)scene.lookup("#btn0");
			Button btn1 = (Button)scene.lookup("#btn1");
			Button btn2 = (Button)scene.lookup("#btn2");
			Button btn3 = (Button)scene.lookup("#btn3");
			Button btn4 = (Button)scene.lookup("#btn4");
			Button btn5 = (Button)scene.lookup("#btn5");
			Button btn6 = (Button)scene.lookup("#btn6");
			Button btn7 = (Button)scene.lookup("#btn7");
			Button btn8 = (Button)scene.lookup("#btn8");
			Button btn9 = (Button)scene.lookup("#btn9");
			Button btnCall = (Button)scene.lookup("#btnCall");
			tf = (TextField)scene.lookup("#tf");
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					Alert alert = new Alert(AlertType.INFORMATION);
					alert.setTitle("지금은");
					alert.setHeaderText("calling~~\n");
					String str = tf.getText();
					alert.setContentText(str);
					alert.show();
				}
			});
			// 기본 작성 형태
//			btn0.setOnMouseClicked(new EventHandler<Event>() {
//				@Override
//				public void handle(Event event) {
//					String tmp= tf.getText();
//					tmp += btn0.getText();
//					tf.setText(tmp);
//				}
//			});

			
			// 람다식 작성 형태 
			// 함수 인터페이스의 경우에는 호출 메서드가 하나 밖에 없기 때문에 
			// 그 메서드가 호출될 때 자동으로 판단하게 됨
			btn0.setOnMouseClicked((Event event) -> {
				myclick("0");
			});
			btn1.setOnMouseClicked((Event event) -> {
				myclick("1");
			});
			btn2.setOnMouseClicked((Event event) -> {
				myclick("2");
			});
			btn3.setOnMouseClicked((Event event) -> {
				myclick("3");
			});
			btn4.setOnMouseClicked((Event event) -> {
				myclick("4");
			});
			btn5.setOnMouseClicked((Event event) -> {
				myclick("5");
			});
			btn6.setOnMouseClicked((Event event) -> {
				myclick("6");
			});
			btn7.setOnMouseClicked((Event event) -> {
				myclick("7");
			});
			btn8.setOnMouseClicked((Event event) -> {
				myclick("8");
			});
			btn9.setOnMouseClicked((Event event) -> {
				myclick("9");
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}
	
	public void myclick(String num) {
		String str_new = num;
		String str_old = tf.getText();
		
		tf.setText(str_old + str_new);
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
	
	
	
}
