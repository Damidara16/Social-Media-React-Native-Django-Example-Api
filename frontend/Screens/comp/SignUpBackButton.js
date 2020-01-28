import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, Switch, Picker } from 'react-native';




export default class BackButton extends React.Component {
  constructor(props){
    super(props);
    this.state = {};
  }

  componentDidMount(){
    console.log('new');
  }



  render() {
    return (
      <View style={{height:50,width:'100%'}}>
        <Button title='back' onPress={()=>this.props.navigation.goBack()} />
      </View>
    );
  }
}


const styles = StyleSheet.create({

});
