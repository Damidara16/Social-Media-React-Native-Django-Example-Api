import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, Switch, Picker } from 'react-native';
import BackButton from './comp/SignUpBackButton';


export default class ProfileEditScreen extends React.Component {
  constructor(props){
    super(props);
    this.state = {bio:'',
    link1:'',
    link2:'',
    location:'',
    private:null,
    celeb:false,
    plus18:false};
  }


  profileAction = () => {
    fetch('http://127.0.0.1:8000/account/update/profile/',{method:'post',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body:JSON.stringify({bio:this.state.bio, link1:this.state.link1, link2:this.state.link2,
      location:this.state.location, private:this.state.private,
      plus18:this.state.plus18})}).then(res=>res.json()).then(res=>{console.log(res)})
  }

  componentDidMount(){
    console.log('create profile');
  }

  render() {
    return (

      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
      {JSON.stringify(this.props.navigation.getParam('back', false)) ? <BackButton navigation={this.props.navigation}/> : null}

      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='bio' autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>
      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='link' autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>
      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='link' autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>
      <TextInput style={{width:'90%', height:50, backgroundColor:'grey', borderRadius:5}} placeholder='location' autoCorrect={false} keyboardType="email-address" textContentType="emailAddress" onChangeText={(text)=>{this.setState({email:text})}}/>
      <View style={{height:10}}></View>

      <View style={{flexDirection:'row', height:50, width:'90%',justifyContent:'space-around', alignItems:'center', backgroundColor:'red', borderRadius:5}}>
        <Text>Content 18 Plus</Text><Switch onValueChange={val=>this.setState({plus18:val})} value={this.state.plus18}></Switch>
      </View>
      <View style={{height:10}}></View>

      <View style={{flexDirection:'row', height:50, width:'90%',justifyContent:'space-around', alignItems:'center', backgroundColor:'red', borderRadius:5}}>
        <Text>Private Account</Text><Switch onValueChange={val=>this.setState({plus18:val})} value={this.state.plus18}></Switch>
      </View>

      <Button title='sign up' onPress={()=>this.profileAction()}></Button>
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
