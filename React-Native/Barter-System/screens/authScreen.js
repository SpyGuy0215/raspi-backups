import * as React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Dimensions, Alert } from 'react-native';


export default class AuthScreen extends React.Component {
	constructor() {
		super()
		this.state={
			email: '',
			password: ''
		}
	}

	userSignIn = () => {
		firebase.auth.signInWithEmailAndPassword(this.state.email, this.state.password)
		.catch(function(error){
			let errorMessage = error.message 
			return Alert.alert(errorMessage)
		})
	}


	render() {
		return(
			<View style={styles.container}>
				<TextInput onChangeText={(text) => {this.setState({email: text})}} style={styles.textinput} placeholder='Email'/>
				<TextInput onChangeText={(text) => {this.setState({password: text})}}style={styles.textinput} placeholder='Password'/>
				<TouchableOpacity style={styles.touchableopacity}>
					<Text>Sign Up</Text>
				</TouchableOpacity>
				<TouchableOpacity onPress={this.userSignIn} style={styles.touchableopacity}>
					<Text>Sign In</Text>
				</TouchableOpacity>
			</View>
		)
	}
}

const styles = StyleSheet.create({
	container:{
		marginTop: 30
	},
	textinput:{
		borderWidth: 1,
		marginBottom: 20,
		width: Dimensions.get('window').width/1.5,
		alignSelf: 'center'
	},
	touchableopacity:{
		alignSelf: 'center',
		marginBottom: 30
	}
	
})