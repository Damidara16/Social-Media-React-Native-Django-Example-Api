import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, Switch, Picker } from 'react-native';



export default class SignUpScreen extends React.Component {
  constructor(props){
    super(props);
    this.state = {email:'',password1:'', password2:'', dob:'', uname:'',};
  }


  signUp = () => {
    if (this.state.password1 !== this.state.password2){
      this.setState({errors:''})
      //force update
    } else {
    fetch('http://127.0.0.1:8000/account/create/user/',{method:'post',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body:JSON.stringify({email:this.state.email, password:this.state.password, date_of_birth:this.state.dob, username:this.state.uname})}).then(res=>res.json()).then(res=>{console.log(res)})
  }}

  componentDidMount(){
    console.log('create user');
  }


  render() {
    return (

      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
      <Button title='home' onPress={()=>this.props.navigation.navigate('Pre')} />

      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='email' autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>
      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='username' autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>
      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='password' textContentType="password" secureTextEntry={true} onChangeText={(text)=>{this.setState({password:text})}}/>
      <View style={{height:10}}></View>
      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='confirm password' textContentType="password" secureTextEntry={true} onChangeText={(text)=>{this.setState({password:text})}}/>
      <View style={{height:10}}></View>
      <Button title='continue' onPress={()=>this.props.navigation.navigate('profile', {back:true})}></Button>
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
