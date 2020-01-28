import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity } from 'react-native';
import AntDesign from 'react-native-vector-icons/AntDesign';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';


export default class ContentHeader extends React.Component {

constructor(props){
  super(props);
}

  render() {
    const HEIGHT = 40;
    return (
          <View style={{height:HEIGHT,flexDirection:'row'}}>
            <View style={{flex:3 ,justifyContent:'flex-start',alignItems:'center', flexDirection:'row', paddingLeft:10}}>
              <TouchableOpacity>
                <Image style={{width:30, height: 30, borderRadius:30/2}} source={{uri:this.props.PicLink}}/>
              </TouchableOpacity>

            <View style={{paddingLeft:5,justifyContent:'center',  alignItems:'flex-start'}}>
              <TouchableOpacity><Text style={{fontSize:13, fontWeight:"600"}}>{this.props.uname}</Text></TouchableOpacity>
              <Text style={styles.textS}>{this.props.date}</Text>
            </View>
            </View>
            <View style={{flex:1, justifyContent:'center', alignItems:'flex-end'}}>
              <TouchableOpacity>
                <MaterialCommunityIcons name='dots-vertical' size={20} color='black'/>
              </TouchableOpacity>
            </View>
          </View>
    );
  }
}


const styles = StyleSheet.create({
  textS:{fontSize:10}
});
