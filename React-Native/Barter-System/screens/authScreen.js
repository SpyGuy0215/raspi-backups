import * as React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Dimensions } from 'react-native';

export default class AuthScreen extends React.Component {
	render() {
		return(
			<View style={styles.container}>
				<TextInput style={styles.textinput} placeholder='Email'/>
				<TextInput style={styles.textinput} placeholder='Password'/>
				<TouchableOpacity style={styles.touchableopacity}>
					<Text>Sign Up</Text>
				</TouchableOpacity>
				<TouchableOpacity style={styles.touchableopacity}>
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