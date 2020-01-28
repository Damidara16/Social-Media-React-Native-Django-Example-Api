import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, Switch, Picker } from 'react-native';



export default class LoginScreen extends React.Component {
  constructor(props){
    super(props);
    this.state = {email:'',password:''};
  }

  login = () => {
    fetch('http://127.0.0.1:8000/account/auth/',{method:'post',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body:JSON.stringify({email:this.state.email, password:this.state.password})}).then(res=>res.json()).then(res=>{
      if (res['outcome'] !== 'success'){
        console.log(res)
      } else {
        console.log(res['token'])
        this.props.navigation.navigate('App')
      }
    })
  }

  componentDidMount(){
    console.log('login');
  }



  render() {
    return (

      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
      <Button title='home' onPress={()=>this.props.navigation.navigate('Pre')} />
      <TextInput autoCapitalize='none' placeholderTextColor="white" style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5, color:'white'}} placeholder={this.props.placeholder} autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>
      <TextInput placeholderTextColor="white" style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5,  color:'white'}} placeholder={this.props.placeholder} textContentType="password" secureTextEntry={true} onChangeText={(text)=>{this.setState({password:text})}}/>
      <Button title='login' onPress={()=>this.login()}></Button>
      </View>

    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#ecf0f1',
    padding: 8,
    alignItems:'center'
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});
