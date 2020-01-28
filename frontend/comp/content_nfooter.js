import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image, Picker, FlatList } from 'react-native';
import QPost from '../../content/QPostComp';
import ContentHeader from '../../comp/content_header'
import displayDate from '../../app_funcs';
import AntDesign from 'react-native-vector-icons/AntDesign';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import Ionicon from 'react-native-vector-icons/Ionicons';



export default class NFooter extends React.Component {
  constructor(props){
    super(props);
    this.state = {comment:true};
    this.data;
  }

  APIAction = () => {
    fetch('http://127.0.0.1:8000/feed/notif/',{method:'get',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + TOKEN
    }}).then(res=>res.json()).then(res=>{
      if (res['outcome'] !== 'success'){
        console.log('error');
      } else {
        this.data=res.data;
        this.setState({});

        //this.forceUpdate();

      }
    })
  }

  componentDidMount(){
    console.log('notif')
  }


  render() {
    const HEIGHT = 40;
    if (this.state.comment === true ){

        com=<View style={{height:75, backgroundColor:'blue'}}>
            <Text numberOfLines={5} style={{fontSize:20, paddingHorizontal:10, paddingTop:5}}>sdf ereoiro reiorjrn{this.state.text}</Text>
          </View>;
        } else {com = <View></View>}
    return (

          <View style={{width:'95%',backgroundColor:'white', borderBottomLeftRadius:20, borderBottomRightRadius:20}}>
          {/*header*/}
          <View style={{height:HEIGHT+10,flexDirection:'row', backgroundColor:'red'}}>
            <View style={{flex:3 ,justifyContent:'flex-start',alignItems:'center', flexDirection:'row', paddingLeft:10}}>
              <TouchableOpacity>
                <Image style={{width:40, height: 40, borderRadius:40/2}} source={{uri:'https://steemitimages.com/DQmcTPPhEtbgqDFQxC7i7riRU53BkCwUW8881ta4AoSQ58L/taylor-swift-most-beautiful-woman.jpg'}}/>
              </TouchableOpacity>

            <View style={{paddingLeft:5,justifyContent:'center',  alignItems:'flex-start'}}>
              <TouchableOpacity><Text style={{fontSize:13, fontWeight:"600"}}>taylor swift{this.props.uname}</Text></TouchableOpacity>
              <Text style={styles.textS}>20 hours ago{this.props.date}</Text>
            </View>
            </View>
            <View style={{flex:1, justifyContent:'center', alignItems:'flex-end'}}>
              <TouchableOpacity>
                <MaterialCommunityIcons name='dots-vertical' size={20} color='black'/>
              </TouchableOpacity>
            </View>
          </View>

          {com}

            <View style={{height:HEIGHT, flexDirection:'row', backgroundColor:'red'}}>
                  <View style={{flex:2, flexDirection:'row', justifyContent:'flex-start',alignItems:'center', paddingLeft:10, paddingTop:5}}>
                    <TouchableOpacity style={{justifyContent:'center', alignItems:'center', flexDirection:'row', paddingRight:10}}>
                    <Ionicon name="ios-heart" size={25} color={this.props.liked ? 'red' : 'black'} />
                    <Text style={{paddingLeft:5}}>20{this.props.numLikes}</Text>
                    </TouchableOpacity>

                    <TouchableOpacity style={{justifyContent:'center', alignItems:'center', flexDirection:'row', paddingRight:10}}>
                    <Ionicon style={styles.icons} name="ios-text" size={25} color='black' />
                    <Text style={{paddingLeft:5}}>33{this.props.numComs}</Text>
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

          </View>
    );
  }
}



const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 10,
  },
  item: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 32,
  },
});
