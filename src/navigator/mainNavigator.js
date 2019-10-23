import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

import SplashScreen from "../features/SplashScreen";

import { GoogleMapsNavigator } from "../features/MapsScreen/navigator";
import CalendarNavigator from "../features/Calendar/navigator";
import TutorialNavigator from "../features/Tutorial/navigator";
import { MessengerNavigator } from "../features/Messenger/navigator";
import {EmailAuthNavigator} from '../features/EmailAuth/navigator';
import { CameraNavigator } from "../features/UserCamera/navigator";

//@BlueprintImportInsertion

/**
 * new navigators can be imported here
 */

const AppNavigator = createStackNavigator(
  {
    SplashScreen: {
      screen: SplashScreen
    },
    
    MapsScreen: {
      screen: GoogleMapsNavigator
    },
    
    
    Calendar: {
      screen: CalendarNavigator
    },
    
    
    EmailAuth: {
      screen: EmailAuthNavigator,
    },
    
    
    Tutorial: {
      screen: TutorialNavigator
    },
    
    
    UserCamera: {
      screen: CameraNavigator
    },
    
    
    Messenger: {
      screen: MessengerNavigator
    },
    

    //@BlueprintNavigationInsertion

    /** new navigators can be added here */
  },
  {
    initialRouteName: 'SplashScreen',
    headerMode: 'none' /** you can play with this */,
  },
);

const AppContainer = createAppContainer(AppNavigator);

export default AppContainer;
