/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.ranger.entity;

import org.apache.ranger.common.AppConstants;
import org.apache.ranger.common.RangerCommonEnums;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;

import java.util.Objects;

@Entity
@Table(name = "x_user_module_perm")
public class XXUserPermission extends XXDBBase implements java.io.Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @SequenceGenerator(name = "X_USER_MODULE_PERM_SEQ", sequenceName = "X_USER_MODULE_PERM_SEQ", allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.AUTO, generator = "X_USER_MODULE_PERM_SEQ")
    @Column(name = "ID")
    protected Long id;

    @Column(name = "USER_ID", nullable = false)
    protected Long userId;

    @Column(name = "MODULE_ID", nullable = false)
    protected Long moduleId;

    @Column(name = "IS_ALLOWED", nullable = false)
    protected Integer isAllowed;

    public XXUserPermission() {
        isAllowed = RangerCommonEnums.IS_ALLOWED;
    }

    /**
     * @return the userId
     */
    public Long getUserId() {
        return userId;
    }

    /**
     * @param userId the userId to set
     */
    public void setUserId(Long userId) {
        this.userId = userId;
    }

    /**
     * @return the moduleId
     */
    public Long getModuleId() {
        return moduleId;
    }

    /**
     * @param moduleId the moduleId to set
     */
    public void setModuleId(Long moduleId) {
        this.moduleId = moduleId;
    }

    /**
     * @return the isAllowed
     */
    public Integer getIsAllowed() {
        return isAllowed;
    }

    /**
     * @param isAllowed the isAllowed to set
     */
    public void setIsAllowed(Integer isAllowed) {
        this.isAllowed = isAllowed;
    }

    @Override
    public int getMyClassType() {
        return AppConstants.CLASS_TYPE_RANGER_USER_PERMISSION;
    }

    /**
     * @return the id
     */
    public Long getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(Long id) {
        this.id = id;
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        } else if (!super.equals(obj)) {
            return false;
        }

        XXUserPermission other = (XXUserPermission) obj;

        return Objects.equals(id, other.id) &&
                Objects.equals(isAllowed, other.isAllowed) &&
                Objects.equals(moduleId, other.moduleId) &&
                Objects.equals(userId, other.userId);
    }

    @Override
    public String toString() {
        String str = "VXUserPermission={";
        str += super.toString();
        str += "id={" + id + "} ";
        str += "userId={" + userId + "} ";
        str += "moduleId={" + moduleId + "} ";
        str += "isAllowed={" + isAllowed + "} ";
        str += "}";

        return str;
    }
}
