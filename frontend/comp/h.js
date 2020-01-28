import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/Octicons';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import Ionicon from 'react-native-vector-icons/Ionicons';


export default class ContentFooter extends React.Component {

  constructor(props){
    super(props);
  }

  render() {
    const HEIGHT = 40;
    return (
      <View style={{height:HEIGHT, flexDirection:'row'}}>
            <View style={{flex:2, flexDirection:'row', justifyContent:'flex-start',alignItems:'center', paddingLeft:10, paddingTop:5}}>
              <TouchableOpacity style={{justifyContent:'center', alignItems:'center', flexDirection:'row'}}>
              <Ionicon name="ios-heart" size={25} color={this.props.liked ? 'red' : 'black'} />
              <Text style={{paddingLeft:5}}>{this.props.numLikes}</Text>
              </TouchableOpacity>

              <TouchableOpacity style={{justifyContent:'center', alignItems:'center', flexDirection:'row'}}>
              <Ionicon style={styles.icons} name="ios-text" size={25} color='black' />
              <Text style={{paddingLeft:5}}>{this.props.numComs}</Text>
              </TouchableOpacity>

              <TouchableOpacity>
              <Ionicon style={styles.icons} name="ios-share-alt" size={25} color='black' />
              </TouchableOpacity>


            </View>
            <View style={{flex:2,alignItems:'center', flexDirection:'row', justifyContent:'flex-end', paddingRight:10, paddingTop:5}}>
              <TouchableOpacity>
              <Ionicon style={styles.icons} name="ios-bookmark" size={25} color='black' />
              </TouchableOpacity>
            </ View>
      </View>
    );
  }
}


const styles = StyleSheet.create({
  icons:{paddingLeft:10}
});
