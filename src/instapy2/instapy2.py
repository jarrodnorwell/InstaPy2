from .utilities import LoggerConstants, Utility
from .types import CommentType, LikeType

from datetime import datetime
from random import choice, randint
from typing import Union

class InstaPy2(Utility):
    def comment(self, amount: int, iterable: list[Union[int, None] | str], type: CommentType):
        self.logger.error(message='THIS IS A WIP REWORK. PLEASE USE `MAIN`.')
        exit(0)

        match type:
            case CommentType.HASHTAG:
                for elem in iterable:
                    hashtag = str(elem)

                    identifiers = self.persistence.all_identifiers(table='medias_comments_hashtag')
                    medias = self.medias.get_medias_for_hashtag(amount=amount, hashtag=hashtag, identifiers_to_skip=identifiers)

                    for media in medias:
                        if not self.is_media_validated_for_interaction(media=media):
                            self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                        else:
                            self.logger.info(message=LoggerConstants.MEDIA_VALID)
                            if not self.persistence.identifier_exists(table='medias_comments_hashtag', identifier=media.id):
                                if not randint(a=0, b=100) <= self.comments.percentage:
                                    self.logger.error(message=LoggerConstants.PERCENTAGE_OUT_OF_BOUNDS)
                                else:
                                    try:
                                        commented = self.session.media_comment(media_id=media.id, text=choice(seq=self.comments.comments)) is not None
                                        if not commented:
                                            self.logger.error(message=LoggerConstants.MEDIA_COMMENT_FAIL)
                                        else:
                                            self.persistence.insert_identifier(table='medias_comments_hashtag', identifier=media.id, timestamp=datetime.now())
                                            self.logger.info(message=LoggerConstants.MEDIA_COMMENT_SUCCESS)
                                    except:
                                        self.logger.error(message=LoggerConstants.MEDIA_COMMENT_FAIL)
                            else:
                                pass
                        

    def like(self, amount: int, iterable: list[Union[int, None] | str], type: LikeType):
        self.logger.error(message='THIS IS A WIP REWORK. PLEASE USE `MAIN`.')
        exit(0)

        match type:
            case LikeType.HASHTAG:
                for element in iterable:
                    hashtag = str(element)

                    identifiers = self.persistence.all_identifiers(table='medias_likes_hashtag')
                    medias = self.medias.get_medias_for_hashtag(amount=amount, hashtag=hashtag, identifiers_to_skip=identifiers)

                    for media in medias:
                        if not self.is_media_validated_for_interaction(media=media):
                            self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                        else:
                            self.logger.info(message=LoggerConstants.MEDIA_VALID)
                            if not self.persistence.identifier_exists(table='medias_likes_hashtag', identifier=media.id):
                                try:
                                    liked = self.session.media_like(media_id=media.id)
                                    if not liked:
                                        self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                    else:
                                        self.persistence.insert_identifier(table='medias_likes_hashtag', identifier=media.id, timestamp=datetime.now())
                                        self.logger.info(message=LoggerConstants.MEDIA_LIKE_SUCCESS)
                                except:
                                    self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                            else:
                                pass
            case LikeType.LOCATION:
                for elem in iterable:
                    location = self.get_pk(query=input('Enter a location name (eg: Bondi Beach, New South Wales): ')) if elem is None else int(elem)

                    if location is None:
                        self.logger.error(message=f'An error occurred while scraping media for location: {location}.')
                    else:
                        identifiers = self.persistence.all_identifiers('medias_likes_location')
                        medias = self.medias.get_medias_for_location(amount=amount, location=location, identifiers_to_skip=identifiers)

                        for media in medias:
                            if not self.is_media_validated_for_interaction(media=media):
                                self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                            else:
                                self.logger.info(message=LoggerConstants.MEDIA_VALID)
                                if not self.persistence.identifier_exists(table='medias_likes_location', identifier=media.id):
                                    try:
                                        liked = self.session.media_like(media_id=media.id)
                                        if not liked:
                                            self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                        else:
                                            self.persistence.insert_identifier(table='medias_likes_location', identifier=media.id, timestamp=datetime.now())
                                            self.logger.info(message=LoggerConstants.MEDIA_LIKE_SUCCESS)
                                    except:
                                        self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                else:
                                    pass
            case LikeType.USER:
                for elem in iterable:
                    username = str(elem)

                    identifiers = self.persistence.all_identifiers(table='medias_likes_user')
                    medias = self.medias.get_medias_for_user(amount=amount, username=username, identifiers_to_skip=identifiers)

                    if medias is None:
                        self.logger.error(message=f'An error occurred while scraping media for user: {username}.')
                    else:
                        for media in medias:
                            if not self.is_media_validated_for_interaction(media=media):
                                self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                            else:
                                self.logger.info(message=LoggerConstants.MEDIA_VALID)
                                if not self.persistence.identifier_exists(table='medias_likes_user', identifier=media.id):
                                    try:
                                        liked = self.session.media_like(media_id=media.id)
                                        if not liked:
                                            self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                        else:
                                            self.persistence.insert_identifier(table='medias_likes_user', identifier=media.id, timestamp=datetime.now())
                                            self.logger.info(message=LoggerConstants.MEDIA_LIKE_SUCCESS)
                                    except:
                                        self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                else:
                                    pass