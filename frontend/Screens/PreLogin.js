import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, Switch, Picker } from 'react-native';


export default class PreLoginScreen extends React.Component {

  constructor(props){
    super(props);
    LROUTE = 'Login';
    SROUTE = 'SignUp';
  }

  componentDidMount(){
    console.log('pre');
  }
  render() {
    return (
      <View style={{flex:1,backgroundColor:'white'}}>
      <StatusBar backgroundColor="blue" barStyle="dark-content" hidden={false}/>
      <View style={{flex:1, justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:60,fontWeight:'700',paddingTop:50}}>Fanmojis</Text>
      </View>

      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
        <TouchableOpacity onPress={()=>this.props.navigation.navigate(LROUTE)} style={{width:'90%',height:'20%',backgroundColor:'blue',justifyContent:'center', alignItems:'center', borderRadius:5}}>
          <Text style={{fontSize:30,fontWeight:'700'}}>Login</Text>
        </TouchableOpacity>
        <View style={{height:30}}></View>
        <TouchableOpacity onPress={()=>this.props.navigation.navigate(SROUTE)} style={{width:'90%',height:'20%',backgroundColor:'blue',justifyContent:'center', alignItems:'center', borderRadius:5}}>
          <Text style={{fontSize:30,fontWeight:'700'}}>Sign Up</Text>
        </TouchableOpacity>
      </View>

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
