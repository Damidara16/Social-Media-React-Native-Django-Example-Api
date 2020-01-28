import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity } from 'react-native';
import ContentHeader from './comp/content_header';
import ContentFooter from './comp/content_footer';


export default class Poster extends React.Component {

  constructor(props){
    super(props);
    this.state = {title:'',brief:'',uuid:null};
    this.header = {proPic:'',uname:'',date:null};
    this.footer = {numLikes:0,numComs:0,liked:false,saved:false};
  }
  render() {
    return (
      <View style={{flex:1, justifyContent:'center', alignItems:'center'}}>
        <View style={{width:'100%',backgroundColor:'white', borderRadius:5}}>
          <ContentHeader PicLink={this.header.proPic} uname={this.header.uname} date={this.header.date} uuid={this.state.uuid}/>

          <TouchableOpacity style={{height:100}}>
            <Text numberOfLines={1} style={{fontSize:30, fontWeight:'bold', paddingHorizontal:10, paddingTop:5}}>
            {this.state.title}
            </Text>
            <View style={{height:10}}></View>
            <Text numberOfLines={2} style={{fontSize:14, paddingHorizontal:10}}>
            {this.state.brief}
            </Text>
          </TouchableOpacity>

          <ContentFooter numComs={this.footer.numComs} numLikes={this.footer.numLikes} liked={this.footer.liked} saved={this.footer.saved} uuid={this.state.uuid}/>
        </View>
</View>
    );
  }
}


const styles = StyleSheet.create({

});
