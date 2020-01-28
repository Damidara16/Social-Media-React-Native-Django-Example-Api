import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity,FlatList } from 'react-native';
import Icon from 'react-native-vector-icons/Octicons';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import Ionicon from 'react-native-vector-icons/Ionicons';

Comment = () => {
  const DA = {
    id:1,
    id:2,
    id:3
  }
  {/*    <FlatList
  data={DA}
  keyExtractor={item => item.id}
  ItemSeparatorComponent = {<View style={{backgroundColor:'green', height:20}}></View>}
  renderItem={({ item }) => {<View style={{backgroundColor:'green', height:20}}></View>}}
      />
  */}
  return (

  <View style={{width:'100%', height:100, backgroundColor:'red'}}>
    <View style={{backgroundColor:'green', height:20}}></View>
    <View style={{backgroundColor:'blue', height:20}}></View>
    <View style={{backgroundColor:'green', height:20}}></View>
    <View style={{backgroundColor:'blue', height:20}}></View>
  </View>
  );
}
export default class ContentFooter extends React.Component {

  constructor(props){
    super(props);
    this.state = {comment:false, show:false};
    this.data;
  }

  render() {
    const HEIGHT = 40;
    const COLOR = 'black';
    if (this.state.comment === true || this.props.c ){

        com=<View style={{height:this.props.h ? this.props.h : 95, backgroundColor:''}}>
            <Text numberOfLines={4} style={{fontSize:18, color:COLOR, paddingHorizontal:10, paddingTop:5}}>sdf ereoiro reiorjrn efi eiwo ffke fioenf eoi fk ioef eiofj fioewf foienf ewfioefnf efoiwenf fofinewf ewfewoifnewf ewfiojewfe foifnwef wefoiewfw{this.state.text}</Text>
          </View>;
        } else {com = null}
    return (
      <View style={{width:'95%'}}>
          <View style={this.props.qp === true ? styles.s2 : styles.s1}>
          {/*header*/}
          <View style={{height:HEIGHT+10,flexDirection:'row', backgroundColor:''}}>
            <View style={{flex:3 ,justifyContent:'flex-start',alignItems:'center', flexDirection:'row', paddingLeft:10}}>
              <TouchableOpacity>
                <Image style={{width:40, height: 40, borderRadius:40/2}} source={{uri:'https://steemitimages.com/DQmcTPPhEtbgqDFQxC7i7riRU53BkCwUW8881ta4AoSQ58L/taylor-swift-most-beautiful-woman.jpg'}}/>
              </TouchableOpacity>

            <View style={{paddingLeft:5,justifyContent:'center',  alignItems:'flex-start'}}>

              <TouchableOpacity><Text style={{fontSize:13, fontWeight:"600", color:COLOR}}>taylor swift{this.props.uname}</Text></TouchableOpacity>
              <Text style={{color:COLOR}}>20 hours ago{this.props.date}</Text>
            </View>
            </View>
            <View style={{flex:1, justifyContent:'center', alignItems:'flex-end'}}>
              <TouchableOpacity>
                <MaterialCommunityIcons name='dots-vertical' size={20} color={COLOR}/>
              </TouchableOpacity>
            </View>
          </View>

          {com}

            <View style={{height:HEIGHT, flexDirection:'row', backgroundColor:''}}>
                  <View style={{flex:2, flexDirection:'row', justifyContent:'flex-start',alignItems:'center', paddingLeft:10, paddingTop:5}}>
                    <TouchableOpacity style={{justifyContent:'center', alignItems:'center', flexDirection:'row', paddingRight:10}}>
                    <Ionicon name="ios-heart" size={25} color={this.props.liked ? 'red' : 'red'} />
                    <Text style={{paddingLeft:5,color:COLOR}}>20{this.props.numLikes}</Text>
                    </TouchableOpacity>

                    <TouchableOpacity onPress={()=>{this.setState({show:!this.state.show})}} style={{justifyContent:'center', alignItems:'center', flexDirection:'row', paddingRight:10}}>
                    <Ionicon style={styles.icons} name="ios-text" size={25} color={COLOR} />
                    <Text style={{paddingLeft:5, color:COLOR}}>33{this.props.numComs}</Text>
                    </TouchableOpacity>

                    <TouchableOpacity>
                    <Ionicon style={styles.icons} name="ios-share-alt" size={25} color={COLOR} />
                    </TouchableOpacity>


                  </View>
                  <View style={{flex:2,alignItems:'center', flexDirection:'row', justifyContent:'flex-end', paddingRight:10, paddingTop:5}}>
                    <TouchableOpacity>
                    <Ionicon style={styles.icons} name="ios-bookmark" size={25} color={COLOR} />
                    </TouchableOpacity>
                  </ View>
            </View>
          </View>

          {this.state.show ? <Comment/> : null}
          </View>
    );
  }
}

const styles = StyleSheet.create({
  icons:{paddingLeft:10},
  s1:{width:'100%',backgroundColor:'#ffffff', borderBottomLeftRadius:20, borderBottomRightRadius:20},
  s2:{width:'100%',backgroundColor:'#ffffff', borderBottomLeftRadius:20, borderBottomRightRadius:20, borderTopLeftRadius:20, borderTopRightRadius:20,}
});
