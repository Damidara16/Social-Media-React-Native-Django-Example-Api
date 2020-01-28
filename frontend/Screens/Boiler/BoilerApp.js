import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, Switch, Picker } from 'react-native';


{/*
  <Scroller />


allpost:{user, linktodetail, date, numoflikes, numofcom, ifcurrliked}
poster:{postTitle,postShortDis,}
tweet:{tweetcontent}
image:{imageurl}
*/}


export default class AppName extends React.Component {
  constructor(props){
    super(props);
    this.state = {};
  }

  APIAction = () => {
    fetch('http://127.0.0.1:8000/account/auth/',{method:'post',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body:JSON.stringify({})}).then(res=>res.json()).then(res=>{console.log(res)})
  }

  componentDidMount(){
    console.log('new');
  }



  render() {
    return (
      <View style={{flex:1,backgroundColor:'white'}}>

      </View>
    );
  }
}


const styles = StyleSheet.create({

});
